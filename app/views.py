from rest_framework.viewsets import ModelViewSet

from app.permissions import EmployeePermission, EmployeeReadPermission
from app.serializers import UserSerializer, EmployeeSerializer
from app.models import Employee
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated, AllowAny
User = get_user_model()


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_superuser:
            return self.queryset
        else:
            return self.queryset.filter(email=user.email)


class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [EmployeePermission | EmployeeReadPermission]

    def get_queryset(self):
        user = self.request.user
        if self.request.user.is_superuser:
            return self.queryset.filter(is_delete=False).order_by('id')
        else:
            return self.queryset.filter(employees__email=user.email)

    def perform_create(self, serializer):
        data = self.request.data
        obj = serializer.save()

        user = User()
        user.employee = obj
        user.username = data['username']
        user.email = data['email']
        password = data['password']
        user.set_password(password)
        user.save()
