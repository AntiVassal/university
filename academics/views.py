from django.contrib.auth.decorators import login_required
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import filters, viewsets

from .filters import CourseFilter
from .forms import CourseForm
from .models import Course, Major
from .serializers import CourseSerializer, MajorSerializer
from users.decorators import role_required
from users.permissions import IsAdminOrReadOnly


class MajorViewSet(viewsets.ModelViewSet):
    queryset = Major.objects.order_by('name')
    serializer_class = MajorSerializer
    permission_classes = [IsAdminOrReadOnly]


@extend_schema_view(
    list=extend_schema(
        tags=['courses'],
        summary='List courses (filter / search / order)',
    ),
    retrieve=extend_schema(tags=['courses']),
)
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('department').order_by('name')
    serializer_class = CourseSerializer
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = CourseFilter
    search_fields = ['name', 'department__name']
    ordering_fields = ['name', 'credits']
    ordering = ['name']


def home(request):
    return render(request, 'academics/index.html')


@login_required(login_url='users:login')
def course_list(request):
    courses = Course.objects.select_related('department')

    department = request.GET.get('department')
    if department:
        courses = courses.filter(department__name=department)

    return render(request, 'academics/course_list.html', {
        'courses': courses,
        'selected_department': department,
    })


@login_required(login_url='users:login')
def course_detail(request, pk):
    course = get_object_or_404(Course.objects.select_related('department'), pk=pk)
    enrollments = course.enrollments.select_related('student')
    return render(request, 'academics/course_detail.html', {
        'course': course,
        'enrollments': enrollments,
    })


@login_required(login_url='users:login')
@role_required('admin')
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save()
            return redirect('academics:course_detail', pk=course.pk)
    else:
        form = CourseForm()

    return render(request, 'academics/course_form.html', {'form': form})
