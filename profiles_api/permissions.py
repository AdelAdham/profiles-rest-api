from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to updte only their own status"""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to updte their own statu"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
