from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
# from Main.api.serializers import UserSerializer, TrackSerializer, AlbumSerializer, PlaylistSerializer, \
#     UserMusicSerializer, FriendSerializer, FriendshipRequestSerializer
from Main.api.serializers import UserSerializer
from Main.models import Track, Album, Playlist, UserMusic


class UserViewSet(viewsets.ModelViewSet):
    '''
    API endpoint, allows users to be viewed or edited
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TrackViewSet(viewsets.ModelViewSet):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class AlbumViewSet(viewsets.ModelViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PlaylistViewSet(viewsets.ModelViewSet):

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class UserMusicViewSet(viewsets.ModelViewSet):

    queryset = UserMusic.objects.all()
    serializer_class = UserMusicSerializer


class FriendViewSet(viewsets.ModelViewSet):

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendshipRequestViewSet(viewsets.ModelViewSet):

    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer


# class UserListAPIView(ListAPIView):
#     model = User
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         return User.objects.all()