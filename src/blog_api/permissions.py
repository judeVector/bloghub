from rest_framework.permissions import BasePermission, SAFE_METHODS


class PostUserWritePermission(BasePermission):
    """Editing posts is restricted to the author only."""

    message = "Editing posts is restricted to the author only."

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user
