from django.shortcuts import get_object_or_404, render

from .models import Course


def home(request):
    return render(request, 'academics/index.html')


def course_list(request):
    courses = Course.objects.select_related('department')

    department = request.GET.get('department')
    if department:
        courses = courses.filter(department__name=department)

    return render(request, 'academics/course_list.html', {
        'courses': courses,
        'selected_department': department,
    })


def course_detail(request, pk):
    course = get_object_or_404(Course.objects.select_related('department'), pk=pk)
    enrollments = course.enrollments.select_related('student')
    return render(request, 'academics/course_detail.html', {
        'course': course,
        'enrollments': enrollments,
    })
