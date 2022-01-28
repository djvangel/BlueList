from django.db import models
from django.utils.text import slugify
# Create your models here.


class Genero(models.Model):  # TAG Franquicia
    nombre_genero = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, null=True, blank=True, unique=True)
    # titulo ForeingKey

    class Meta:
        ordering = ['nombre_genero']

    def save(self, *args, **kwargs):  # luego agregamos esta funcion a la clase para que se agrege el titulo como slug
        self.slug = slugify(self.nombre_genero)
        super(Genero, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_genero


class Estado(models.TextChoices):  # TAG Titulo
    FINALIZADO = "Finalizado"
    EMISION = "Emision"
    PROXIMAMENTE = "Proximamente"


class Formato(models.TextChoices):  # TAG Titulo
    ANIME = "Anime"
    MANGA = "manga"
    PELICULA = "pelicula"
    TVSHOW = "TVshow"
    SERIE = "serie"


class Estacion(models.TextChoices):  # TAG Titulo
    INVIERNO = "Invierno"
    PRIMAVERA = "Primavera"
    VERANO = "Verano"
    OTOÑO = "Otoño"
