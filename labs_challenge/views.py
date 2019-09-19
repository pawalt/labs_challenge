import requests
from bs4 import BeautifulSoup
from labs_challenge.models import Club, Tag
from django.views.generic import View
from django.http import HttpResponse
import subprocess


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

        return HttpResponse(status=204)


class ASCIIView(View):
    def get(self, request):
        url = request.GET.get('image-url')
        output = subprocess.check_output(['jp2a', url])
        return HttpResponse(output)
