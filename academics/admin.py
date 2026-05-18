from django.contrib import admin

from .models import Course, Major


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'credits']
    list_filter = ['department']
    search_fields = ['name']
