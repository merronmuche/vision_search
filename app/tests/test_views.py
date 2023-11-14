




from django.test import TestCase

from app.models import Image

class ImageModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Image.objects.create(title='dog')

    def test_create_feature_vector(self):
        im = Image.objects.get(id=1)
        pass
    
    



