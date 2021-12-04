from django.shortcuts import render
from .models import Office
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contact(request):
    offices = Office.objects.all()
    print(len(offices))
    context = {
        'offices':offices
    }
    return render(request, 'main/contact.html', context)

def about_us(request):
    return render(request, 'main/about_us.html')