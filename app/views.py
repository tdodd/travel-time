# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

import urllib2, json
from .models import Location

# Google Maps API Constants
API_KEY = 'AIzaSyBDw6Ac70Y8ctrz1nkx1_y8IaF8U05SbQc'
API_ENDPOINT_GEOCODE = 'https://maps.googleapis.com/maps/api/geocode/json'
API_ENDPOINT_DISTANCE = 'https://maps.googleapis.com/maps/api/distancematrix/json'

"""
Homepage
"""
def index(request):
   if request.method == "GET" :
      try:
         # Get all Locations from db
         locations = Location.objects.all()

         # Add Locations to context
         context = {
            'locations': locations
         }

         # Send response to client
         return render(request, 'index.html', context)

      except ObjectDoesNotExist:
         # If db is empty
         context = {}

         # Send response to client
         return render(request, 'index.html', context)
   
   else :
      return render(request, 'bad-request.html')

"""
Location
"""

# Create Location
def create_location(request):
   if request.method == "POST" :
      # Get place_id
      p_id = get_place_id(request)

      # Create new Location
      l = Location(
         address = request.POST['address'],
         city = request.POST['city'],
         province = request.POST['province'],
         place_id = p_id
      ).save()

      # Send response to client
      return redirect('/', permanent=True)

   else :
      return render(request, 'bad-request.html')

# Get place_id for a given address
def get_place_id(request):
   # Get location data from request
   # and replace spaces with '+'
   addr = request.POST['address'].replace(" ", "+")
   cty = request.POST['city'].replace(" ", "+")
   prov = request.POST['province'].replace(" ", "+")
   
   # Build query to send to Google
   params = '?address=' + addr + ',' + cty + ',' + prov + '&key=' + API_KEY
   query = API_ENDPOINT_GEOCODE + params

   # Get coordinates from maps API using urllib2
   # and convert from str to json
   google_response = json.loads(urllib2.urlopen(query).read())

   # Extract place_id from response
   place_id = [key['place_id'] for key in google_response['results']]
   return place_id[0]

# Update Location
def update_location(request, locationID):
    return render(request, 'index.html', { 'header_text': header_text })

# Delete Location
def delete_location(request, location_id):
   Location.objects.filter(id=location_id).delete()
   return redirect('/')