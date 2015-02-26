from friendship.models import Friend, FriendshipRequest
from Main.models import Track, UserMusic, Album, Playlist

from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username', 'email', 'first_name', 'last_name', 'password')
        write_only_fields = ('password',)

    def create(self, attrs, instance=None):
        # call set_password on user object. Without this
        # the password will be stored in plain text.
        user = super(UserSerializer, self).create(attrs)
        user.set_password(attrs['password'])
        user.save()
        return user


    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     return instance



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