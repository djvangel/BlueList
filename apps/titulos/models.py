from django.db import models
from django.utils.text import slugify
from ..tags.models import Estado, Genero, Formato

# Create your models here.


class Franquicia(models.Model):  # one pice / vengadores / teoria del big bang
    """ Hace referencia a un universo general de en las que pueden hacer apariciones de varias historias
    en distintas presentaciones"""
    nombre_franquicia = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True, null=True)  # Post foreikey

    # titulos = ForeignKey()

    # TAGs
    genero = models.ManyToManyField(Genero, related_name='franquicia', blank=True)

    # MEDIA
    banner = models.URLField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)

    actualizado = models.DateTimeField(auto_now=True, blank=True)  # Ultima actualizacion
    # Logica Url

    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre_franquicia)
        super(Franquicia, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_franquicia

    class Meta:
        ordering = ["id"]


class Titulo(models.Model):  # tempora 1 / live action / civil war / manga / comic
    """ Presentacion del universo o franquicia, manga, serie, liveaction, etc"""

    nombre_titulo = models.CharField(max_length=255)
    publicacion = models.DateField(null=True, blank=True)  # dia que se publico el film
    """#### agregar descripcio"""
    sinopsis = models.TextField(blank=True, null=True)

    # TAGs
    estado = models.CharField(max_length=50, choices=Estado.choices)
    # puede ser un manga, una entrega, una pelicula, de un mismo titulo
    formato = models.CharField(max_length=50, choices=Formato.choices)
    genero = models.ManyToManyField(Genero, related_name='titulos', blank=True)

    # foreingkey
    franquicia = models.ForeignKey(Franquicia, related_name='titulos', on_delete=models.CASCADE, null=True, blank=True)
   
    # Personajes
    # entregas
    # comentarios

    """ MEDIA """
    imagen = models.URLField(blank=True, null=True)
    banner = models.URLField(blank=True, null=True)
    clip = models.URLField(blank=True, null=True)

    # Logica Url
    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre_titulo)
        super(Titulo, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_titulo

    class Meta:
        ordering = ["franquicia", "publicacion"]  # se ordenan por obras


class Personaje(models.Model):
    """ Descipcion completa del personaje, links que se consideren importantes, sus interpretes"""

    nombre_personaje = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    imagen = models.URLField(blank=True, null=True)

    # Titulo donde aparece  // si borran ese titulo desaparese este personaje
    obra = models.ManyToManyField(Titulo, related_name='personajes', blank=True)

    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre_personaje)
        super(Personaje, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_personaje

    class Meta:
        ordering = ["obra__nombre_titulo"]  # se ordenan por los nombres de la clave foranea manyToMany


class Entrega(models.Model):  # Capitulo , parte, capitulo manga, estreno de pelicula
    """ se refiera a la presentacion individual de alguna fanquicia, capitulos, corto, largometraje etc"""
    numero = models.IntegerField(blank=True, null=True)
    """ los numeros se comparten con todo tipo de entregas diferentes """
    nombre_entrega = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True, null=True)
    titulo = models.ForeignKey(Titulo, related_name='entregas', on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.URLField(blank=True, null=True)
    # links
    # comentarios

    def __str__(self):
        return self.nombre_entrega

    slug = models.SlugField(max_length=255, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.nombre_entrega)
        super(Entrega, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.numero) + " " + str(self.titulo)

    class Meta:
        ordering = ['titulo', 'numero']  # Ayudara a ordernar los datos a la hora de registrar
