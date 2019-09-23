from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from labs_challenge.views import ClubsView, ScrapeView, ASCIIView, FavoriteView, UserView


admin.site.site_header = 'Pennlabs Example Admin'

urlpatterns = [
    # Normal URL Patterns go here
    path('admin/', admin.site.urls),
    path('accounts/login/', auth_views.LoginView.as_view()),
    path('accounts/', include('django.contrib.auth.urls')),
    path('scrape', ScrapeView.as_view()),
    path('ascii', ASCIIView.as_view()),
    path('api/clubs', ClubsView.as_view()),
    path('api/favorite', FavoriteView.as_view()),
    path('api/user/<slug:username>', UserView.as_view())
]
