from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import viewsets

from .forms import DepartmentForm
from .models import Department, Student
from .serializers import DepartmentSerializer, StudentSerializer
from users.decorators import role_required


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.select_related('chairperson')
    serializer_class = DepartmentSerializer


class StudentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.select_related('major')
    serializer_class = StudentSerializer


def home(request):
    return render(request, 'students/index.html')


@login_required(login_url='users:login')
def department_list(request):
    departments = Department.objects.select_related('chairperson').all()
    return render(request, 'students/department_list.html', {
        'departments': departments,
    })


@login_required(login_url='users:login')
def department_detail(request, pk):
    department = get_object_or_404(
        Department.objects.select_related('chairperson'),
        pk=pk,
    )
    return render(request, 'students/department_detail.html', {
        'department': department,
    })


@login_required(login_url='users:login')
@role_required('admin')
def department_create(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            department = form.save()
            return redirect('students:department_detail', pk=department.pk)
    else:
        form = DepartmentForm()

    return render(request, 'students/department_form.html', {'form': form})
