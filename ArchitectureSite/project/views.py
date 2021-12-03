from django.shortcuts import render
from .models import Property

# Create your views here.
def project_index(request):

    propertys = Property.objects.all()

    context ={
        'propertys':propertys,
    }
    return render(request, 'project/project_index.html', context)

