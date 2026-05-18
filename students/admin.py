from django.contrib import admin

from .models import Department, Sudent


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'chairperson']
    search_fields = ['name', 'chairperson__username']


@admin.register(Sudent)
class SudentAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'major']
    list_filter = ['major']
    search_fields = ['first_name', 'last_name', 'email']
