from django.db import models

# Create your models here.

from django.utils.text import slugify


class Genero(models.Model):# TAG Franquicia
    nombre_genero = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,null=True, blank=True, unique=True)     
    # titulo ForeingKey
    class Meta:
        ordering = ['nombre_genero'] 

    def save(self, *args, **kwargs):    #luego agregamos esta funcion a la clase para que se agrege el titulo como slug
        self.slug = slugify(self.nombre_genero)
        super(Genero, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_genero

class Estado(models.TextChoices): #TAG Titulo
    FINALIZADO = "Finalizado"
    EMISION = "Emision"
    PROXIMAMENTE = "Proximamente"

class Formato(models.TextChoices):#TAG Titulo
    ANIME = "Anime"
    MANGA = "manga"
    PELICULA = "película"
    TVSHOW = "TVshow"
    SERIE = "serie"

class Estacion(models.TextChoices):#TAG Titulo
    INVIERNO = "Invierno"
    PRIMAVERA = "Primavera"
    VERANO = "Verano"
    OTOÑO = "Otoño"
#TAG-END


class Franquicia(models.Model): # one pice / vengadores / teoria del big bang
    nombre_franquicia = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True , null=True) # Post foreikey
    # titulos = ForeignKey() # 
    #TAG
    genero = models.ManyToManyField(Genero, related_name='franquicia', blank=True)
    # MEDIA

    banner= models.URLField(blank=True, null=True)
    imagen= models.URLField(blank=True, null=True)

    # LOGICA
    actualizado = models.DateTimeField(auto_now=True, blank=True)  # Ultima actualizacion

    #Logica Url
    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_franquicia)
        super(Franquicia, self).save(*args, **kwargs) 
    
    def __str__(self):
        return self.nombre_franquicia
    

class Titulo(models.Model): # tempora 1 / live action / civil war / manga / comic
    nombre_titulo = models.CharField(max_length=255)
    publicacion = models.DateField(null=True, blank=True) # dia que se publico el film
    #TAGs
    estado = models.CharField(max_length=50, choices=Estado.choices)
    formato = models.CharField(max_length=50, choices=Formato.choices) # puede ser un manga, una entrega, una pelicula, de un mismo titulo
    
    # foreiking
    franquicia = models.ForeignKey(Franquicia, related_name='titulos', on_delete=models.CASCADE, null=True, blank=True)
    # staff                       
    # entregas
    # comentarios


    """ MEDIA """
    imagen1 = models.URLField(blank=True , null=True)
    imagen2 = models.URLField(blank=True , null=True)
    banner = models.URLField(blank=True , null=True)
    clip = models.URLField(blank=True , null=True)

    """Openings Links agregados por la comunidad, sera otro campo tipo links"""
   

    #Logica Url
    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_titulo)
        super(Titulo, self).save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_titulo


class Staff(models.Model):
    nombre_staff = models.CharField(max_length=255)
    cargo = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True) # redes sociales, otros trabajos / links a Staff en otra instancia
    imagen= models.URLField(blank=True, null=True)


    # se crearan varias entradas de una misma persona, por si realiza otros trabajos en otras franquicias
    obra = models.ForeignKey(Titulo, related_name='staff', on_delete=models.CASCADE, null=True, blank=True)


    # personaje que interpreta o encarna:

    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_staff)
        super(Staff, self).save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_staff


class Personaje(models.Model):
    nombre_personaje = models.CharField(max_length=255)
    bio = models.TextField(blank=True, null=True)
    links = models.TextField(blank=True, null=True) # temas de interes
    imagen= models.URLField(blank=True, null=True)

    # Titulo donde aparece  // si borran ese titulo desaparese este personaje
    obra = models.ForeignKey(Titulo, related_name='personaje', on_delete=models.CASCADE, null=True, blank=True)
    # interpete
    interprete = models.ForeignKey(Staff, related_name='personaje', on_delete=models.CASCADE, blank=True, null=True) 
    """ solucionar: un personaje puede ser interpretado por varios actores de doblaje dependiendo del idioma"""


    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_personaje)
        super(Personaje, self).save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_personaje


class Entrega(models.Model): # Capitulo , parte, capitulo manga, estreno de pelicula
    numero = models.IntegerField(blank=True, null=True)
    nombre_entrega = models.CharField(max_length=255)
    sinopsis = models.TextField(blank=True, null=True)
    titulo = models.ForeignKey(Titulo, related_name='entrega', on_delete=models.CASCADE, null=True, blank=True)
    imagen= models.URLField(blank=True, null=True)
    
    # links

    """ NO NECESITA media solo comentarios"""
    # comentarios

    def __str__(self):
        return self.nombre_entrega


    slug = models.SlugField(max_length=255, blank=True) 
    def save(self, *args, **kwargs):    
        self.slug = slugify(self.nombre_entrega)
        super(Entrega, self).save(*args, **kwargs) 

    def __str__(self):
        return self.nombre_entrega


class LinksEntregas(models.Model): # aporte de la comunidad
    url = models.URLField() 
    entrega = models.ForeignKey(Entrega, related_name='links', on_delete=models.CASCADE, null=True, blank=True)
    """Agregar* sistema de votos"""
    

    def __str__(self):
        return " link " + str(self.entrega) + " " + str(self.id) 