from django.contrib import admin
from .models import Property, PropertyImage, PropertyType
# Register your models here.
admin.site.register(Property)
admin.site.register(PropertyType)
admin.site.register(PropertyImage)