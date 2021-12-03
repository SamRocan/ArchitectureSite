from django.shortcuts import render, redirect, get_object_or_404
from .models import Job, JobAppilcation
from .forms import JobApplicationForm
# Create your views here.
def career_index(request):
    job_roles = Job.objects.all()
    context = {
        'jobs':job_roles
    }
    return render(request, 'career/career_index.html', context)

def job_application(request, jobID):
    job_role = get_object_or_404(Job, id=jobID)

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data['first_name'])
            form.save()
            return redirect('index')
    else:
        form = JobApplicationForm()

    context = {
        'job_role':job_role,
        'form':form
    }
    return render(request, 'career/job_application.html', context)