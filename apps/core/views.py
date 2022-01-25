from django.shortcuts import render
from ..titulos.models import Titulo
# Create your views here.


def home(request):
    titulos = Titulo.objects.all()
    ctx = {"titulos": titulos}

    return render(request, 'core/home.html', ctx )


def registro(request):
    return render(request, 'core/registro.html')


def login(request):
    return render(request, 'core/login.html')


def titulo(request):
    return render(request, 'titulo/titulo.html')

def franquicia(request):
    return render(request, 'titulo/franquicia.html')

def entrega(request):
    return render(request, 'titulo/entrega.html')


def staff(request):
    return render(request, 'titulo/staff.html')





def capitulo(request):
    return render(request, 'titulo/capitulo.html')