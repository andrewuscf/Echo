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


# class SavedPlaylists(models.Model):
#     user = models.ForeignKey(CustomUser)

# class FriendRequest(models.Model):
#     invite = models.BooleanField(default=False)
#     request = models.BooleanField(default=False)
#     sender = models.ForeignKey(User, related_name="sent_request")
#     recipient = models.ForeignKey(User, related_name="received_request")
#     message = models.CharField(max_length=256, blank=True)
#     new = models.BooleanField(default=True)
#     time_created = models.DateTimeField(default=timezone.now)
#
#     class Meta:
#         verbose_name = _('Friendship Request')
#
#     def __unicode__(self):
#         return "User #{} friendship requested #{}".format(self.sender, self.recipient)
#
#     def accept

# Music
class Artist(models.Model):
    name = models.CharField(max_length=60)


class Album(models.Model):
    name = models.CharField(max_length=60)


class Song(models.Model):
    name = models.CharField(max_length=60)
    album = models.ForeignKey(Album, null=True, blank=True)
    artist = models.ForeignKey(Artist, null=True, blank=True)
    url = models.TextField(blank = True, null = True)
    image_url = models.TextField(blank = True, null = True)
    duration = models.CharField(max_length = 10, blank = True, null = True)
    release_year = models.SmallIntegerField(max_length = 4, blank = True, null=True)

class Playlist(models.Model):
    name = models.CharField(max_length=60)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User)