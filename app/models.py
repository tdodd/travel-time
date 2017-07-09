# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class Location(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=30)
    longitude = models.FloatField()
    latitude = models.FloatField()

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    locations = models.ManyToManyField(Location)