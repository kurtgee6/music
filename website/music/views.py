# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Album

def index(request):
    # connection to the database
    all_albums = Album.objects.all()

    #dictionary
    context = {
        'all_albums': all_albums
    }

    #rendering html page
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + " </h2>" )