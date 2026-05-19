from rest_framework import serializers

from academics.models import Course
from academics.serializers import CourseSerializer
from students.models import Student
from students.serializers import StudentSerializer

from .models import CustomUser, Enrollment


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'department']


class EnrollmentSerializer(serializers.ModelSerializer):
    student = StudentSerializer(read_only=True)
    student_name = serializers.CharField(
        source='student.__str__',
        read_only=True,
    )
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        source='student',
        write_only=True,
    )
    course = CourseSerializer(read_only=True)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',
        write_only=True,
    )

    class Meta:
        model = Enrollment
        fields = [
            'id',
            'student',
            'student_name',
            'student_id',
            'course',
            'course_id',
            'term',
        ]
