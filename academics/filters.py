from django_filters import rest_framework as filters

from students.models import Department

from .models import Course


class CourseFilter(filters.FilterSet):
    min_credits = filters.NumberFilter(field_name='credits', lookup_expr='gte')
    max_credits = filters.NumberFilter(field_name='credits', lookup_expr='lte')
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    department = filters.ModelChoiceFilter(queryset=Department.objects.all())

    class Meta:
        model = Course
        fields = ['department']
