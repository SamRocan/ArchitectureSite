from django.shortcuts import render

# Create your views here.
def career_index(request):
    context = {

    }
    return render(request, 'career/career_index.html', context)