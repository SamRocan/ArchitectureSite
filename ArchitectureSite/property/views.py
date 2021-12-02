from django.shortcuts import render

# Create your views here.
def property_index(request):

    context ={

    }
    return render(request, 'property/property_index.html', context)