from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def project_index(request):

    context ={

    }
    return render(request, 'project/project_index.html', context)

