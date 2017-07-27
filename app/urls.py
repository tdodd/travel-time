from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^$', views.LocationListView.as_view()),

    # /location
    url(r'^locations$', views.LocationListView.as_view()),

    # /location/12345
    url(r'^location/([0-9]+)$', views.delete_location),

    # /trips
    url(r'^trips$', views.get_trips),

    # /travel-time
    url(r'^travel-time$', views.get_travel_time),
]