from django import forms
from .models import Property, PropertyImages


class PropertyForm(forms.ModelForm):

    class Meta:
        model = Property
        fields = ('name', 'street_address', 'city', 'country', 'post_code', 'PropertyType',)


class PropertyImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image')
    class Meta:
        model = PropertyImages
        fields = ('image', )