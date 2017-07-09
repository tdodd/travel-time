# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist

from .models import Location, User

"""
Homepage
"""
def index(request):
    return render(request, 'index.html')

"""
Location
"""

# Create Location
def createLocation(request):
    # create    
    return render(request, 'index.html', { 'header_text': header_text })

# Get Location
def getLocation(request, locationID):
    # read
    return render(request, 'index.html', { 'header_text': header_text })

# Update Location
def updateLocation(request, locationID):
    # update
    return render(request, 'index.html', { 'header_text': header_text })

# Delete Location
def deleteLocation(request, locationID):
    # delete
    return render(request, 'index.html', { 'header_text': header_text })

"""
User
"""

# Create user
def createUser(request):
    # create    
    return render(request, 'index.html', { 'header_text': header_text })

# Get user
def getUser(request, userID):
    
    try:
        user = User.objects.get(id=userID)
        locations = user.locations.all()
        context = {
            'user': user,
            'locations': locations
        }
        return render(request, 'index.html', context)
    
    except ObjectDoesNotExist:
        context = {
            'error': "Oops. Something went wrong :("
        }
        return render(request, 'index.html', context)

# Update user
def updateUser(request, userID):
    # update
    return render(request, 'index.html', { 'header_text': header_text })

# Delete user
def deleteUser(request, userID):
    # delete
    return render(request, 'index.html', { 'header_text': header_text })