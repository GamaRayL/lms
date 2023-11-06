from users.models import UserRoles
from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoles.MODERATOR


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRoles.MEMBER:
            return obj.owner == request.user
        return False
