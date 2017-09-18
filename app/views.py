from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.list import ListView

import os, urllib2, json

from models import Location, Trip
from travel_time import env

# Google Maps API Constants
API_ENDPOINT_GEOCODE = 'https://maps.googleapis.com/maps/api/geocode/json'
API_ENDPOINT_DISTANCE = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric'

"""
Homepage: GET /locations
"""
class LocationListView(ListView):
    model = Location
    template_name = 'index.html'
    context_object_name = 'locations'

"""
Trips: GET /trips
"""
def get_trips(request):
   locations = Location.objects.all()
   trips = Trip.objects.all()
   context = {
      'location_list': locations,
      'trip_list': trips
   }
   return render(request, 'trips.html', context)

"""
Location
"""
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
   params = '?address=' + addr + ',' + cty + ',' + prov + '&key=' + env.API_KEY
   query = API_ENDPOINT_GEOCODE + params

   # Get coordinates from maps API using urllib2
   # and convert from str to json
   google_response = json.loads(urllib2.urlopen(query).read())

   # Extract place_id from response
   place_id = [key['place_id'] for key in google_response['results']]
   return place_id[0]

# Delete Location
def delete_location(request, location_id):
   Location.objects.filter(id=location_id).delete()
   return redirect('/')

"""
Travel Time
"""
def get_travel_time(request):
   # Get address data from request
   from_text = request.POST['from']
   to_text = request.POST['to']

   # Get place_ids from db
   origin = Location.objects.get(address=from_text).place_id
   destination = Location.objects.get(address=to_text).place_id

   # Build query to send to Google
   params = '&origins=place_id:' + origin + '&destinations=place_id:' + destination + '&key=' + env.API_KEY
   query = API_ENDPOINT_DISTANCE + params

   # Get travel time from maps API using urllib2
   # and convert from str to json
   google_response = json.loads(urllib2.urlopen(query).read())
   
   # Extract travel time from response
   travel_time = [key['elements'][0]['duration']['text'] for key in google_response['rows']]
   travel_time = travel_time[0]

   # Get page data
   locations = Location.objects.all()
   trips = Trip.objects.all()
   
   context = {
      'location_list': locations,
      'trip_list': trips,
      'travel_time': travel_time,
      'origin': from_text,
      'destination': to_text
   }

   return render(request, 'trips.html', context)