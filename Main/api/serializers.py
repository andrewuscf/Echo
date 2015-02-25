from friendship.models import Friend, FriendshipRequest
from Main.models import Track, UserMusic, Album, Playlist, UserPlaylistTrack, UserPicture

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('name', 'source', 'album', 'previewURL', 'playlists', 'type')


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('name', 'artist', 'views', 'likes', 'type')


class PlaylistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playlist
        fields = ('title', 'user', 'type')


class UserMusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMusic
        fields = ('user',)


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('to_user', 'from_user', 'created', 'objects')


class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        # fields = ('')


class UserPlaylistTrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaylistTrack


class UserPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPicture