from django import forms
from .models import JobAppilcation

class JobApplicationForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'type':'email', 'class': 'form-control',  'placeholder':'test'}))
    cover_letter = forms.FileField(widget=forms.FileInput(attrs={'type':'file', 'class': 'custom-file-input', 'id':'cover-letter'}))
    cv = forms.FileField(widget=forms.FileInput(attrs={'type':'file', 'class': 'custom-file-input', 'id':'cv'}))
    portfolio = forms.FileField(widget=forms.FileInput(attrs={'type':'file', 'class': 'custom-file-input', 'id':'portfolio'}))

    class Meta:
        model = JobAppilcation
        fields = ['first_name', 'last_name','email','cover_letter','cv','portfolio']