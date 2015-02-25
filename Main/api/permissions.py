from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated


class IsOwnerOrReadOnly(permissions.BasePermission):
    # Only allows the user who owns an object to edit it.

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user


class IsMainFriendOrReadOnly(permissions.BasePermission):
    # Allows user (you) to edit friend and friend request objects
    # Forbids other users from editing, but allows them to view friends
    # Prevents anonymous users from viewing

    def has_object_permission(self, request, view, obj):

        if request.user.is_authenticated():

            if request.method in permissions.SAFE_METHODS:
                return True

            return obj.from_user == request.user


class IsOwnerOnly(permissions.BasePermission):
    # Only allows the user associated with object to view or edit

    def has_object_permission(self, request, view, obj):

        return obj.user == request.user