from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<userID>[0-9]+)/$', views.getUser),
    url(r'^$', views.index),
]