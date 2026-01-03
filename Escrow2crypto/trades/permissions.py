from rest_framework.permissions import BasePermission

class IsAdminUserOnly(BasePermission):
    """
    Custom permission to only allow admin users to access certain views.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_staff