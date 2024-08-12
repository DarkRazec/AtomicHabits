from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """
    Checks whether user is object owner or superuser
    """
    def has_object_permission(self, request, view, obj) -> bool:
        return request.user == obj.user or request.user.is_superuser
