from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'core/home.html')


def registro(request):
    return render(request, 'core/registro.html')


def login(request):
    return render(request, 'core/login.html')


def titulo(request):
    return render(request, 'titulo/titulo.html')


def staff(request):
    return render(request, 'titulo/staff.html')





def capitulo(request):
    return render(request, 'titulo/capitulo.html')