from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.career_index, name='career_index'),
    path('<int:jobID>/', views.job_application, name='job_application')
]