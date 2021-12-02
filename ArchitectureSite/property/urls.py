from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.property_index, name='property_main')
]