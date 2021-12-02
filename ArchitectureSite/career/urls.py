from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.career_index, name='career_index')
]