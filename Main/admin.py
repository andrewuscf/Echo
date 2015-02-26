from django.contrib import admin
from Main.models import Album, Playlist, Track, UserPlaylistTrack, UserPicture, UserStatus

admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Track)
admin.site.register(UserPlaylistTrack)
admin.site.register(UserPicture)
admin.site.register(UserStatus)
