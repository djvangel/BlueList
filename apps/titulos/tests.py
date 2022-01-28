from django.test import TestCase
from . models import Titulo
# Create your tests here.


class TestTitulo(TestCase):
    def setUp(self):  # Construye el objeto a verificar
        self.titulo = Titulo.objects.create(nombre_titulo="testing", formato="Anime", estado="Finalizado")

    def test_titulo_model(self):
        m = self.titulo
        self.assertTrue(isinstance(m, Titulo))
