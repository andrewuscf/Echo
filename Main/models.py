import datetime
from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser, User
from django.db import models


# Create your models here.


# Users

# Make a custom user model
from django.utils import timezone
# AUTH_USER_MODEL = CustomUser

# class CustomUser(AbstractUser):
#
#     class Meta:
#         unique_together = (('username', 'email'),)


# Music
class Album(models.Model):
    name = models.CharField(max_length=128)
    artist = models.CharField(max_length=128)
    image = models.URLField()
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    type = models.CharField(default='album', max_length=128)

    def __unicode__(self):
        return self.name


class Playlist(models.Model):
    title = models.CharField(max_length=128)
    user = models.ForeignKey(User)  # Playlist created by
    type = models.CharField(default='playlist', max_length=128)

    def __unicode__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=128)
    source = models.CharField(max_length=128)
    album = models.ForeignKey(Album)
    previewURL = models.URLField(blank=True)
    playlists = models.ManyToManyField(Playlist, blank=True)
    type = models.CharField(default='track', max_length=128)

    def __unicode__(self):
        return self.name


class UserMusic(models.Model): # This model store user's music
    user = models.OneToOneField(User)


    def __unicode__(self):
        return self.user.username