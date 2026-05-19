from django.db import models
from django.conf import settings


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255, blank=True)
    address = models.CharField(max_length=255, blank=True)
    dob = models.DateField(blank=True, null=True)
    major = models.ForeignKey(
        'academics.Major',
        on_delete=models.PROTECT,
        related_name='students',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Department(models.Model):
    name = models.CharField(max_length=255, blank=True, default=True)
    chairperson = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='chaired_departments',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
