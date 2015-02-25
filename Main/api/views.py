from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from Main.api.permissions import IsOwnerOrReadOnly, IsMainFriendOrReadOnly, IsOwnerOnly
from Main.api.serializers import UserSerializer, TrackSerializer, AlbumSerializer, PlaylistSerializer, \
    UserMusicSerializer, FriendSerializer, FriendshipRequestSerializer, UserPlaylistTrackSerializer, \
    UserPictureSerializer
from Main.models import Track, Album, Playlist, UserMusic, UserPlaylistTrack, UserPicture


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    '''
    API endpoint, allows users to be viewed or edited
    '''
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TrackViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Track.objects.all()
    serializer_class = TrackSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class PlaylistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer


class UserMusicViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = UserMusic.objects.all()
    serializer_class = UserMusicSerializer


class FriendViewSet(viewsets.ModelViewSet):
    permission_classes = [IsMainFriendOrReadOnly]

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer


class FriendshipRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsMainFriendOrReadOnly]

    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer


class UserPlaylistTrackViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = UserPlaylistTrack.objects.all()
    serializer_class = UserPlaylistTrackSerializer


class UserPictureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOnly]

    queryset = UserPicture.objects.all()
    serializer_class = UserPictureSerializer

# class UserListAPIView(ListAPIView):
#     model = User
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         return User.objects.all()