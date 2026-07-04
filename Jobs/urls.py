from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('jobs/', views.job_list, name='jobs'),
    path('job/<int:id>/', views.job_detail, name='job_detail'),
    path('apply/<int:id>/', views.apply_job, name='apply_job'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('', views.home, name='home'),

]

