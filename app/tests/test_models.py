

from django.test import TestCase

from app.models import Image

class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Image.objects.create(title='dog')

    def test_get_absolute_url(self):
        im = Image.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(im.get_absolute_url(), '/images/1/')
    
    



