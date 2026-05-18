from django.urls import path
from . import views


app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('departments/', views.department_list, name='department_list'),
    path('departments/create/', views.department_create, name='department_create'),
    path('departments/<int:pk>/', views.department_detail, name='department_detail'),
]
