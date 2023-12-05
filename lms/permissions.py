from rest_framework.exceptions import PermissionDenied

from users.models import UserRoles
from rest_framework.permissions import BasePermission


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            raise PermissionDenied('У вас недостаточно прав для выполнения данного действия.')
        if request.user.role == UserRoles.MODERATOR:
            return True


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoles.ADMIN


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.role == UserRoles.MEMBER:
            return obj.owner == request.user
        return False
