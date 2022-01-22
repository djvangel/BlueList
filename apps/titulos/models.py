from django.db import models

# Create your models here.





class Formato(models.TextChoices):
    ANIME = "anime"

class Genero(models.TextChoices):
    ACCION = "acción"



class Titulo(models.Model):
    nombreTitulo = models.CharField(max_length=500)
    sinopsis = models.TextField(blank=True , null=True) # Post foreikey
    # temporada = models.ForeignKey() # 

    # TAGS
    formato = models.CharField(max_length=50, choices=Formato.choices)
    genero = models.CharField(max_length=50, choices=Genero.choices)
    
    # MEDIA
    imagen1 = models.URLField(blank=True , null=True)
    imagen2 = models.URLField(blank=True , null=True)
    baner = models.URLField(blank=True , null=True)
    clip = models.URLField(blank=True , null=True)
    # Openings Links agregados por la comunidad


    # LOGICA
    slug = models.SlugField(max_length=500, blank=True) # sera agregada mas adelante

    # Ultima actualizacion
    actualizado = models.DateTimeField(auto_now=True)

    # Claves foraneas
    # Temporadas
    # 





class Temporada(models.Model):
    nombreTemporada = models.CharField

    # estado = models.CharField(max_length=50, choices=Categories.choices) # temporada