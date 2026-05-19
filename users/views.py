from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework import viewsets

from .decorators import role_required
from .models import Enrollment
from .permissions import IsAdminOrReadOnly
from .serializers import CustomUserSerializer, EnrollmentSerializer


class CustomUserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.select_related('department').order_by('email')
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrReadOnly]


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related('student', 'course').order_by(
        'student__last_name',
        'student__first_name',
        'course__name',
    )
    serializer_class = EnrollmentSerializer
    permission_classes = [IsAdminOrReadOnly]


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('users:dashboard')

        return render(request, 'users/login.html', {
            'error': 'Invalid credentials',
        })

    return render(request, 'users/login.html')


def logout_view(request):
    logout(request)
    return redirect('users:login')


@login_required(login_url='users:login')
def dashboard(request):
    if not request.user.is_authenticated:
        return redirect('users:login')

    if request.user.role == 'admin':
        return redirect('users:admin_dashboard')
    return redirect('users:instructor_dashboard')


@login_required(login_url='users:login')
@role_required('admin')
def admin_dashboard(request):
    return render(request, 'users/admin_dashboard.html')


@login_required(login_url='users:login')
@role_required('instructor')
def instructor_dashboard(request):
    return render(request, 'users/instructor_dashboard.html')


def home(request):
    return render(request, 'users/index.html')
