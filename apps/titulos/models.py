from django.db import models

# Create your models here.

from django.utils.text import slugify
from ..tags.models import Estado, Genero, Formato



class Franquicia(models.Model): # one pice / vengadores / teoria del big bang
    """ Hace referencia a un universo general de en las que pueden hacer apariciones de varias historias
    en distintas presentaciones"""

    nombre_franquicia = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True , null=True) # Post foreikey
    
    # titulos = ForeignKey() # 
    #TAG
    genero = models.ManyToManyField(Genero, related_name='franquicia', blank=True)
    
    # MEDIA
    banner= models.URLField(blank=True, null=True)
    imagen= models.URLField(blank=True, null=True)

    

    actualizado = models.DateTimeField(auto_now=True, blank=True)  # Ultima actualizacion
    #Logica Url

    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_franquicia)
        super(Franquicia, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.nombre_franquicia
    
class Staff(models.Model):
    """ Todo tipo de personas que hacen parte para la creacion de el film, actores, directores etc
    un personaje puede ser interpretado por varios actores"""

    nombre_staff = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True) # redes sociales, otros trabajos / links a Staff en otra instancia
    imagen= models.URLField(blank=True, null=True)
    # titulo: donde trabajó
    # personaje: que interpreta o encarna:

    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_staff)
        super(Staff, self).save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_staff

class Titulo(models.Model): # tempora 1 / live action / civil war / manga / comic
    """ Presentacion del universo o franquicia, manga, serie, liveaction, etc"""

    nombre_titulo = models.CharField(max_length=255)
    publicacion = models.DateField(null=True, blank=True) # dia que se publico el film
    #TAGs
    estado = models.CharField(max_length=50, choices=Estado.choices)
    formato = models.CharField(max_length=50, choices=Formato.choices) # puede ser un manga, una entrega, una pelicula, de un mismo titulo
    genero = models.ManyToManyField(Genero, related_name='titulos', blank=True)
    
    # foreingkey
    franquicia = models.ForeignKey(Franquicia, related_name='titulos', on_delete=models.CASCADE, null=True, blank=True)
    staff = models.ManyToManyField(Staff, related_name='staff', blank=True)
    # Personajes                   
    # entregas
    # comentarios

    """ MEDIA """
    imagen1 = models.URLField(blank=True , null=True)
    imagen2 = models.URLField(blank=True , null=True)
    banner = models.URLField(blank=True , null=True)
    clip = models.URLField(blank=True , null=True)

    #Logica Url
    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_titulo)
        super(Titulo, self).save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_titulo

class Personaje(models.Model):
    """ Descipcion completa del personaje, links que se consideren importantes, sus interpretes"""

    nombre_personaje = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True)
    imagen= models.URLField(blank=True, null=True)

    # Titulo donde aparece  // si borran ese titulo desaparese este personaje
    obra = models.ManyToManyField(Titulo, related_name='personajes', blank=True)
    
    
    titulo_interprete1 = models.CharField(blank=True, null=True, max_length=255)
    selec_interprete1 = models.ForeignKey(Staff, related_name='personajes1', on_delete=models.CASCADE, blank=True, null=True) 
    
    titulo_interprete2 = models.CharField(blank=True, null=True, max_length=255)
    selec_interprete2 = models.ForeignKey(Staff, related_name='personajes2', on_delete=models.CASCADE, blank=True, null=True) 
    
    titulo_interprete3 = models.CharField(blank=True, null=True, max_length=255)
    selec_interprete3 = models.ForeignKey(Staff, related_name='personajes3', on_delete=models.CASCADE, blank=True, null=True) 


    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_personaje)
        super(Personaje, self).save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_personaje

class Entrega(models.Model): # Capitulo , parte, capitulo manga, estreno de pelicula
    """ se refiera a la presentacion individual de alguna fanquicia, capitulos, corto, largometraje etc"""
    """ NO NECESITA media solo comentarios"""
    numero = models.IntegerField(blank=True, null=True, unique=True)
    nombre_entrega = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True, null=True)
    titulo = models.ForeignKey(Titulo, related_name='entregas', on_delete=models.CASCADE, null=True, blank=True)
    imagen= models.URLField(blank=True, null=True)
    # links    
    # comentarios

    def __str__(self):
        return self.nombre_entrega

    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_entrega)
        super(Entrega, self).save(*args, **kwargs) 

    def __str__(self):
        return "Capitulo "+ str(self.numero) +" "+ str(self.nombre_entrega)







#  





