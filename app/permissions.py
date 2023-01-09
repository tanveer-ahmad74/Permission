from rest_framework.permissions import BasePermission

METHOD_ALLOW = ('GET', 'POST', 'PUT', 'PATCH', 'DELETE')


class EmployeePermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in METHOD_ALLOW and request.user.is_superuser:
            return True
        else:
            return False


class EmployeeReadPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' in METHOD_ALLOW and request.user.is_authenticated:
            return True
        else:
            return False
