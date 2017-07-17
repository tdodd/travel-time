from django.conf.urls import url

from . import views

urlpatterns = [
    # GET /
    url(r'^$', views.index),

    # POST /location
    url(r'^location$', views.create_location),

    # DELETE /location
    url(r'^location/([0-9]+)$', views.delete_location),
]