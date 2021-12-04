from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Office(models.Model):
    street_address = models.CharField(max_length=255)
    post_code = models.CharField(max_length=20, default="")
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    email = models.EmailField(max_length=255)
    google_map_location = models.CharField(max_length=255, help_text="Go to google maps, find the location you desire and copy the 'share' link")
    display_image = models.ImageField(default='images/office_generic.jpg')

    def __str__(self):
        return str(self.city) + " - " + str(self.post_code)