from django.contrib import admin

from .models import Department, Student


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'chairperson']
    search_fields = ['name', 'chairperson__username']


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'major']
    list_filter = ['major']
    search_fields = ['first_name', 'last_name', 'email']
