import requests
from bs4 import BeautifulSoup
from django.utils.decorators import method_decorator
from labs_challenge.models import Club, Tag
from django.contrib.auth import get_user_model
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
import subprocess
import json


class ScrapeView(View):
    def get_clubs(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        boxes = soup.select("div.box")
        clubs = []

        for box in boxes:
            club_name = box.select(".club-name")[0].get_text()
            description = box.select("em")[0].get_text()
            tags = list(map(lambda tag: tag.get_text(), box.select("div span")))
            clubs.append({
                "name": club_name,
                "description": description,
                "tags": tags
            })

        return clubs

    def get(self, request):
        club_data = self.get_clubs('https://ocwp.pennlabs.org/')
        for club in club_data:
            new_club = Club(name=club['name'], description=club['description'])
            new_club.save()
            for tag in club['tags']:
                new_tag = Tag(name=tag)
                new_tag.save()
                new_club.tags.add(new_tag)

        return HttpResponse('Success')


class ASCIIView(View):
    def get(self, request):
        url = request.GET.get('image-url')
        output = subprocess.check_output(['jp2a', '--width=100', url])
        return HttpResponse(output)


class ClubsView(View):
    def get(self, request):
        clubs = Club.objects.all()
        to_convert = []
        for club in clubs:
            to_add = {}
            to_add['name'] = club.name
            to_add['description'] = club.description
            to_add['tags'] = list(map(lambda tag: tag.name, club.tags.all()))
            to_convert.append(to_add)

        return HttpResponse(json.dumps(to_convert))

    def post(self, request, *args, **kwargs):
        data_raw = request.POST.get('club_data', '')
        club_data = json.loads(data_raw)
        for club in club_data:
            new_club = Club(name=club['name'], description=club['description'])
            new_club.save()
            for tag in club['tags']:
                new_tag = Tag(name=tag)
                new_tag.save()
                new_club.tags.add(new_tag)

        return HttpResponse('Success')


@method_decorator(login_required, 'post')
class FavoriteView(View):
    def post(self, request, *args, **kwargs):
        club_name = request.POST.get('club_name')
        club = get_object_or_404(Club, name=club_name)
        request.user.clubs.add(club)
        return HttpResponse('Success')


class UserView(View):
    def post(self, request, *args, **kwargs):
        uname = kwargs['username']

        user = get_object_or_404(get_user_model(), user_name=uname)
        user_dict = {}
        user_dict['name'] = user.name
        user_dict['username'] = uname
        user_dict['clubs'] = list(map(lambda club: club.name, user.clubs.all()))
