"""
university URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Uncomment next two lines to enable admin:
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from academics.views import CourseViewSet, MajorViewSet
from students.views import DepartmentViewSet, StudentViewSet
from users.views import CustomUserViewSet, EnrollmentViewSet


router = DefaultRouter()
router.register('departments', DepartmentViewSet)
router.register('majors', MajorViewSet)
router.register('courses', CourseViewSet)
router.register('students', StudentViewSet)
router.register('users', CustomUserViewSet)
router.register('enrollments', EnrollmentViewSet)

def hello(request):
    if request.user.is_authenticated:
        user_links = """
            <a href="/users/dashboard/">Dashboard</a> |
            <a href="/users/logout/">Logout</a>
        """
    else:
        user_links = '<a href="/users/login/">Login</a>'

    return HttpResponse(f"""
        <h1>Welcome to University</h1>
        <nav>
            <a href="/academics/courses/">Courses</a> |
            <a href="/students/departments/">Departments</a> |
            {user_links}
        </nav>
    """)

urlpatterns = [
    # Uncomment the next line to enable the admin:
    path('admin/', admin.site.urls),
    path('', hello),
    path('academics/', include('academics.urls')),
    path('students/', include('students.urls')),
    path('users/', include('users.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/docs/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
]
