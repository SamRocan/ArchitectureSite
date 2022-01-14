from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.

class PropertyType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Property(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=255)
    post_code = models.CharField(max_length=10)
    description = models.TextField(max_length=5000, default="")
    PropertyType = models.ForeignKey(PropertyType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def get_image_filename(instance, filename):
    title = instance.property.name
    slug = slugify(title)
    return "property_images/%s-%s" % (slug, filename)

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

    def __str__(self):
        return self.property.name + " - Image (" + str(self.id) + ")"