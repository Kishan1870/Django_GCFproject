from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mark/', views.mark_attendance, name='mark_attendance'),
    path('view/', views.view_attendance, name='view_attendance'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

