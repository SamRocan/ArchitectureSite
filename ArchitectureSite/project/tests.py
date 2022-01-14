from django.test import TestCase
from .models import Property, PropertyType
# Create your tests here.
class ProjectTestCase(TestCase):
    def setUp(self):
        building = PropertyType.objects.create(name='Building')
        Property.objects.create(name='canary wharf',
                                street_address = '1 canada square',
                                city ='london',
                                country = 'united kingdom',
                                post_code = 'se1 1aa',
                                description = '1 canary wharf tower',
                                PropertyType = building)

    def test_project(self):
        building = Property.objects.get(name='canary wharf')
        self.assertEqual(building.city, 'london')
        self.assertEqual(building.PropertyType.name, 'Building')




