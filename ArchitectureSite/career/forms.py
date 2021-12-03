from django import forms
from .models import JobAppilcation

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobAppilcation
        fields = '__all__'