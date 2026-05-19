from rest_framework import serializers

from students.models import Department
from students.serializers import DepartmentSerializer

from .models import Course, Major


class MajorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Major
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True,
    )

    class Meta:
        model = Course
        fields = ['id', 'name', 'department', 'department_id', 'credits']
