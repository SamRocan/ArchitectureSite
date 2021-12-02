from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    requirements = models.CharField(max_length=10000)
    salary = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " ("  + str(self.created_at) + ")"

class JobAppilcation(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cover_letter = models.CharField(max_length=4000, blank=True, null=True)
    cv = models.FileField(upload_to='CVs/')
    portfolio = models.FileField(upload_to='CVs/', blank=True, null=True)


    def __str__(self):
        return self.first_name[0]+ "." +self.last_name + ": " + self.job.title