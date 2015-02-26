from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from . import authentication, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth import login, logout
from Main.api.permissions import IsOwnerOrReadOnly, IsMainFriendOrReadOnly
from Main.api.serializers import UserSerializer, TrackSerializer, AlbumSerializer, PlaylistSerializer, \
    UserMusicSerializer, FriendSerializer, FriendshipRequestSerializer
from Main.models import Track, Album, Playlist, UserMusic
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
    # allow non-authenticated user to create via POST
        return (AllowAny() if self.request.method == 'POST' or "GET"
            else IsStaffOrTargetUser()),


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


class AuthView(APIView):
    authentication_classes = (authentication.QuietBasicAuthentication,)
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
         login(request, request.user)
         return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})

# class UserListAPIView(ListAPIView):
#     model = User
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         return User.objects.all()