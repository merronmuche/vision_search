



from django.core.files import File
from django.test import TestCase
import json
from app.models import Image
from app.views import create_feature_vector

class ImageViewTest(TestCase):

    def setUp(self):
        # create two images to test with
        self.image_file = open('app/static/app/images/mountain.jpg', 'rb')
        self.image_file2 = open('app/static/app/images/meron.jpg', 'rb')
        Image.objects.create(title='mountain', image = File(self.image_file))
        Image.objects.create(title='meron', image = File(self.image_file2))

    def test_create_feature_vector(self):
        # after creating the images in setup method, we call the view function create_feature_vector
        images = Image.objects.all()
        self.assertEqual(images[0].feature_vector, None)
        request = self.client.get('/create/')

        create_feature_vector(request)
        self.assertNotEqual(images[0].feature_vector, None)
        fv = json.loads(images[1].feature_vector)
        self.assertEqual(type(fv), dict)
        self.assertEqual(list(fv.keys()), ['fv'])
        self.assertAlmostEqual(fv['fv'][0], -1.6956108979973425, places=4)
        # self.assertAlmostEqual(fv['fv'][:3], [-1.695610761642456, -1.6660512685775757, -1.7274105548858643])



        
    
    



