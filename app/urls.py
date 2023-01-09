from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app.views import UserViewSet, EmployeeViewSet

router_master = DefaultRouter()
router_master.register('user', UserViewSet, basename='user')
router_master.register('employee', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('', include(router_master.urls)),
]