from rest_framework import serializers
from rest_framework.serializers import Serializer
from app.models import Employee
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'employee']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class EmployeeSerializer(serializers.ModelSerializer):
    user = UserListSerializer(read_only=True, many=True, source='employees')

    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'mobile_number', 'address', 'is_delete', 'user']
