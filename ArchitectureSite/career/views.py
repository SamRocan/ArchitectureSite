from django.shortcuts import render, get_object_or_404
from .models import Job, JobAppilcation
# Create your views here.
def career_index(request):
    job_roles = Job.objects.all()
    context = {
        'jobs':job_roles
    }
    return render(request, 'career/career_index.html', context)

def job_application(request, jobID):
    job_role = get_object_or_404(Job, id=jobID)

    context = {
        'job_role':job_role,
    }
    return render(request, 'career/job_application.html', context)