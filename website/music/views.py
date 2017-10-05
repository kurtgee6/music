# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

#raising a 404 Error
from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    # connection to the database
    all_albums = Album.objects.all()

    #dictionary
    context = {'all_albums': all_albums}

    #rendering html page
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'music/detail.html', {'album': album})