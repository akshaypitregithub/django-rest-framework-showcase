from rest_framework.permissions import SAFE_METHODS, BasePermission


class ReadOnlyAndAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return request.user.username

