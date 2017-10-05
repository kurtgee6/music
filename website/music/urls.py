from django.conf.urls import url
from . import views

urlpatterns = [
    # main page 
    url(r'^$', views.index, name='index'),

    # /music/someID
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail')
]
