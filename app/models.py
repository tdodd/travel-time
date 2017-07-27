from __future__ import unicode_literals
from django.db import models

class Location(models.Model):
   address = models.CharField(max_length=100)
   city = models.CharField(max_length=50)
   province = models.CharField(max_length=30)
   place_id = models.CharField(max_length=255)

class Trip(models.Model):
   from_pid = models.CharField(max_length=255)
   to_pid = models.CharField(max_length=255)
   reminder_time = models.TimeField()
   from_text = models.CharField(max_length=255)
   to_text = models.CharField(max_length=255)