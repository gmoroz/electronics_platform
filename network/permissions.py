from rest_framework import permissions
from django.contrib.auth.models import User


class IsActiveUserPermission(permissions.BasePermission):
    message = "Only active employees can use API"

    def has_permission(self, request, view):
        return request.user and request.user.is_active
