from django.shortcuts import render

# Create your views here.
def project_index(request):

    context ={

    }
    return render(request, 'project/project_index.html', context)