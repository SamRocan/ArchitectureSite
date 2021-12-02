from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    requirements = models.CharField(max_length=10000)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

class JobAppilcation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cover_letter = models.CharField(max_length=4000, blank=True, null=True)
    cv = models.FileField(upload_to='CVs/', blank=True, null=True)
    portfolio = models.FileField(upload_to='CVs/', blank=True, null=True)