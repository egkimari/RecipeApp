from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """Only the author or staff can edit/delete. Everyone can read."""
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        # Works for Recipe & Comment (which both have created_by or author)
        return getattr(obj, 'created_by', getattr(obj, 'author', None)) == request.user or request.user.is_staff


class IsStaffOrReadOnly(permissions.BasePermission):
    """Only staff can create/update/delete. Everyone can read."""
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff
