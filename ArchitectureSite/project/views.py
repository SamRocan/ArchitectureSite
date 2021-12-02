from django.shortcuts import render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import PropertyForm, PropertyImageForm
from .models import PropertyImages

# Create your views here.
def project_index(request):

    context ={

    }
    return render(request, 'project/project_index.html', context)

def create_project(request):
    ImageFormSet = modelformset_factory(PropertyImages,
                                        form=PropertyImageForm, extra=3)
    #'extra' means the number of photos that you can upload   ^
    if request.method == 'POST':

        postForm = PropertyForm(request.POST)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=PropertyImages.objects.none())


        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.user = request.user
            post_form.save()

            for form in formset.cleaned_data:
                #this helps to not crash if the user
                #do not upload all the photos
                if form:
                    image = form['image']
                    photo = PropertyImages(post=post_form, image=image)
                    photo.save()
            # use django messages framework
            messages.success(request,
                             "Yeeew, check it out on the home page!")
            return HttpResponseRedirect("/")
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PropertyForm()
        formset = ImageFormSet(queryset=PropertyImages.objects.none())
    return render(request, 'project/create_project.html', {'postForm': postForm, 'formset': formset})