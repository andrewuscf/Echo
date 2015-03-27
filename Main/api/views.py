from django.contrib.auth.models import User
from friendship.models import Friend, FriendshipRequest
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
from . import authentication, serializers
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from django.contrib.auth import login, logout
from Main.api.permissions import IsOwnerOrReadOnly, IsMainFriendOrReadOnly
from Main.api.serializers import UserSerializer, TrackSerializer, AlbumSerializer, PlaylistSerializer, \
    FriendSerializer, FriendshipRequestSerializer
from Main.models import Track, Album, Playlist, UserPlaylistTrack, UserPicture, UserStatus
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrTargetUser, IsOwnerOnly


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
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class AlbumViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class PlaylistViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title', 'user__username')


class FriendViewSet(viewsets.ModelViewSet):
    permission_classes = [IsMainFriendOrReadOnly]

    queryset = Friend.objects.all()
    serializer_class = FriendSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('from_user__username',)


class FriendshipRequestViewSet(viewsets.ModelViewSet):
    permission_classes = [IsMainFriendOrReadOnly]

    queryset = FriendshipRequest.objects.all()
    serializer_class = FriendshipRequestSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('from_user__username',)


class AuthView(APIView):
    authentication_classes = (authentication.QuietBasicAuthentication,)
    serializer_class = serializers.UserSerializer

    def post(self, request, *args, **kwargs):
         login(request, request.user)
         return Response(UserSerializer(request.user).data)

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


class UserPlaylistTrackViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]

    serializer_class = serializers.UserPlaylistTrackSerializer
    queryset = UserPlaylistTrack.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username', 'title')


class UserPictureViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOnly]

    serializer_class = serializers.UserPictureSerializer
    queryset = UserPicture.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username',)


class UserStatusViewSet(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]

    serializer_class = serializers.UserStatusSerializer
    queryset = UserStatus.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__username',)


class FindFriendViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    serializer_class = serializers.UserSerializer
    queryset=User.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)

# class UserListAPIView(ListAPIView):
#     model = User
#     serializer_class = UserSerializer
#     def get_queryset(self):
#         return User.objects.all()