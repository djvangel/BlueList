from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home' ),
    path('login', login, name='login' ),
    path('registro', registro, name='registro' ),
    path('titulo', titulo, name='titulo' ),
    path('capitulo', capitulo, name='capitulo' ),
    path('staff', staff, name='staff' ),
    path('franquicia', franquicia, name='franquicia' ),
    path('entrega', entrega, name='entrega' ),
]