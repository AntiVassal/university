from django.shortcuts import get_object_or_404, redirect, render

from .forms import DepartmentForm
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


def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('students:department_detail', pk=department.pk)
    else:
        form = DepartmentForm()

    return render(request, 'students/department_form.html', {'form': form})
