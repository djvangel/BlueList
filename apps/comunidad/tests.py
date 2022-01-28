from django.test import TestCase
from .models import Links_comunidad
# Create your tests here.


# class ComunidadTest(TestCase):
#     def setup(self):
#         self.comunidad = Links_comunidad.objects.create(url="www.megaupload.com", descripcion ="sadsa" )
#     def test_links_models(self):
#         model = self.comunidad
#         self.assertTrue(isinstance(model, Links_comunidad))

class TestLinks_comunidad(TestCase):
    def setUp(self):
        self.link = Links_comunidad.objects.create(url="www.megaupload.com", descripcion="sadsa")

    def test_links_models(self):
        obj = self.link
        self.assertTrue(isinstance(obj, Links_comunidad))
        self.assertEqual()
