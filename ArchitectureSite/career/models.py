from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=10000)
    requirements = models.TextField(max_length=10000)
    salary = models.IntegerField(verbose_name="Salary (£)", help_text='Annual')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " ("  + str(self.created_at) + ")"

class JobAppilcation(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    cover_letter = models.FileField(verbose_name="Cover Letter (File)", upload_to='cover_letters/', blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    portfolio = models.FileField(upload_to='portfolios/', blank=True, null=True)


    def __str__(self):
        return self.first_name[0]+ "." +self.last_name + ": " + self.job.title
