from django.contrib.auth.models import AbstractUser
from django.db import models


class SoftDelete(models.Model):
    is_delete = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_delete = True
        self.save()

    def restore(self):
        self.is_delete = False
        self.save()

    class Meta:
        abstract = True


class Employee(SoftDelete):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    mobile_number = models.IntegerField(max_length=15, null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class User(AbstractUser, SoftDelete):
    email = models.EmailField(unique=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True, related_name='employees')

    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = 'Users'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
