from django.db import models

# Create your models here.
from ..titulos.models import Entrega, Titulo


class Links_comunidad(models.Model): # aporte de la comunidad
    url = models.URLField() 
    entrega = models.ForeignKey(Entrega, related_name='links', on_delete=models.CASCADE, null=True, blank=True)
    titulo = models.ForeignKey(Titulo, related_name='links', on_delete=models.CASCADE, null=True, blank=True)
    descripcion = models.CharField(max_length=55)

    """Agregar* sistema de votos"""
    

    def __str__(self):
        return " link " + str(self.entrega) + " " + str(self.id) 
