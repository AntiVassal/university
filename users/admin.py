from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Enrollment


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'role', 'department', 'is_staff']
    list_filter = ['role', 'department', 'is_staff']
    search_fields = ['email', 'first_name', 'last_name']
    ordering = ['email']
    fieldsets = UserAdmin.fieldsets + (
        ('University fields', {'fields': ('role', 'department')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom fields', {'fields': ('email', 'first_name', 'last_name', 'role', 'department')}),
    )


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'course', 'term']
    list_filter = ['course', 'term']
    search_fields = [
        'student__first_name',
        'student__last_name',
        'course__name',
        'term',
    ]
