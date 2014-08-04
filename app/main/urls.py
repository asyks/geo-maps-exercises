from django.conf.urls import patterns, include, url
from django.contrib import admin

from main.views import HomeView, ISSLocationView, PortlandParksView,\
                       retrieve_iss_lat_long, retrieve_portland_basketball_parks

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^iss/', ISSLocationView.as_view(), name='iss_location_view'),
    url(r'^ajax/iss/', retrieve_iss_lat_long, name='retrieve_iss_lat_long'),
    url(r'^hoops/', PortlandParksView.as_view(), name='iss_location_view'),
    url(r'^ajax/hoops/', retrieve_portland_basketball_parks, name='retrieve_portland_basketball_parks'),
    url(r'^$', HomeView.as_view(), name='home_view'),
)
