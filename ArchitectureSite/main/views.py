from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def contact(request):
    return render(request, 'main/contact.html')

def about_us(request):
    return render(request, 'main/about_us.html')