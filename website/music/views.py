# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

def index(request):
    # connection to the database
    all_albums = Album.objects.all()
    html = ''
    
    # for loop to grab each objects in Album
    for album in all_albums:
        
        url = '/music/' + str(album.id) + '/'
        html += '<a href="'+ url +'">'+ album.album_title +'</a><br>'
    return HttpResponse(html)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>" )