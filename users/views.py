from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


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
    return render(request, 'users/dashboard.html')


def home(request):
    return render(request, 'users/index.html')
