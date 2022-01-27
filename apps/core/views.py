from ast import For
from django.shortcuts import render
from ..titulos.models import *
from ..tags.models import Formato
# Create your views here.


def home(request):
    titulos = Titulo.objects.all()
    franquicias = Franquicia.objects.reverse()[:3]
    print(franquicia)
    ctx = {"titulos": titulos, "franquicias": franquicias}

    return render(request, 'core/home.html', ctx )

#  variables globales
def formato(request, formato):
    titulos = Titulo.objects.filter(formato = formato ).all()
    ctx = {"titulos": titulos}
    return render(request, 'core/home.html', ctx)



def titulo(request, slug_titulo):
    titulo = Titulo.objects.get(slug = slug_titulo )
    ctx = {"titulo": titulo}
    return render(request, 'titulo/titulo.html', ctx)


def personaje(request, slug_personaje):
    personaje = Personaje.objects.get(slug = slug_personaje )
    ctx = {"personaje": personaje}
    return render(request, 'titulo/personaje.html', ctx)


def staff(request, slug_staff):  
    staff = Personaje.objects.get(slug = slug_staff )
    ctx = {"staff": staff}  
    return render(request, 'titulo/staff.html')


def franquicia(request):
    return render(request, 'titulo/franquicia.html')


def entrega(request, slug_titulo2, slug_entrega):
    entrega = Entrega.objects.get( titulo__slug = slug_titulo,slug = slug_entrega )
    ctx = {"entrega": entrega}

    return render(request, 'titulo/entrega.html', ctx)






def capitulo(request):
    return render(request, 'titulo/capitulo.html')



def registro(request):
    return render(request, 'core/registro.html')


def login(request):
    return render(request, 'core/login.html')