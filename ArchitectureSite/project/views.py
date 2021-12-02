from django.shortcuts import render

# Create your views here.
def project_index(request):

    context ={

    }
    return render(request, 'property/project_index.html', context)