from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import CustomUserManager


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    role = models.CharField(
        max_length=20,
        choices=[('admin', 'Admin'), ('instructor', 'Instructor')],
        default='instructor',
    )
    department = models.ForeignKey(
        'students.Department',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='staff',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email


class Enrollment(models.Model):
    student = models.ForeignKey(
        'students.Student',
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    course = models.ForeignKey(
        'academics.Course',
        on_delete=models.CASCADE,
        related_name='enrollments',
    )
    term = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.student} - {self.course}"
