from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.project_index, name='project_index'),
    path('create/', views.create_project, name='create_project')
]