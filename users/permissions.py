from rest_framework import permissions
from rest_framework.views import Request, View


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        return request.method == "GET" and obj.id == request.user.id
