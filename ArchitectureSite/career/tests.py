from django.test import TestCase
from .models import Job, JobAppilcation
import datetime
# Create your tests here.
class JobsTestCase(TestCase):
    def setUp(self):
        architect = Job.objects.create(
            title='Architect',
            location='Beijing',
            description='A junior role based in london paying £xxx,xxx',
            requirements='BSc Architecture',
            salary='400000',
            created_at=(datetime.datetime.now())
        )
        architectApp = JobAppilcation.objects.create(
            job = architect,
            first_name = 'Bruce',
            last_name = 'Doe',
            email = 'BDoe@ymail.com',
            cv = '11_St.docx'
        )

    def testJob(self):
        architect = Job.objects.get(title='Architect')
        self.assertEqual(architect.location, 'Beijing')

    def testJobApplication(self):
        architectApp = JobAppilcation.objects.get(email='BDoe@ymail.com')
        self.assertEqual(architectApp.first_name, 'Bruce')
        self.assertEqual(architectApp.cv.url, '/media/11_St.docx')