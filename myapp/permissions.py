from rest_framework.permissions import IsAdminUser

class IsAdminUserPermission(IsAdminUser):
    def has_permission(self, request, view):
        return request.user and request.user.is_staff
