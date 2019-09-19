from django.contrib import admin
from django.urls import include, path
from labs_challenge.views import ScrapeView, ASCIIView


admin.site.site_header = 'Pennlabs Example Admin'

urlpatterns = [
    # Normal URL Patterns go here
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('scrape', ScrapeView.as_view()),
    path('ascii', ASCIIView.as_view())
]
