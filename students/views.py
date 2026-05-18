from django.shortcuts import get_object_or_404, render

from .models import Department


def home(request):
    return render(request, 'students/index.html')


def department_list(request):
    departments = Department.objects.select_related('chairperson').all()
    return render(request, 'students/department_list.html', {
        'departments': departments,
    })


def department_detail(request, pk):
    department = get_object_or_404(
        Department.objects.select_related('chairperson'),
        pk=pk,
    )
    return render(request, 'students/department_detail.html', {
        'department': department,
    })
