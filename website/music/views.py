# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
#raising a 404 Error
from django.shortcuts import render, get_object_or_404
from .models import Album, Song

def index(request):
    # connection to the database
    all_albums = Album.objects.all()

    #dictionary
    context = {'all_albums': all_albums}

    #rendering html page
    return render(request, 'music/index.html', context)

def detail(request, album_id):
    #shortcut of try and except 
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album': album})

def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.is_favorite:
            song.is_favorite = False
        else:
            song.is_favorite = True
        song.save()
    except (KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})

