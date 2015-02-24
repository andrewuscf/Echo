from django.contrib import admin
from Main.models import Album, Playlist, Track, UserMusic, UserPlaylistTrack

admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Track)
admin.site.register(UserMusic)
admin.site.register(UserPlaylistTrack)
