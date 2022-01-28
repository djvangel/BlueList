from django.urls import path
from .views import home, titulo, entrega, formato, personaje, capitulo, staff, franquicia, login, registro

urlpatterns = [
    path('', home, name='home'),
    path('formato/<str:formato>/', formato, name='formato'),
    path('titulo/<str:slug_titulo>/', titulo, name='titulo'),
    path('titulo/<str:slug_titulo>/<str:slug_entrega>/', entrega, name='entrega'),
    path('titulo/<str:slug_titulo>/personajes/<str:slug_personaje>/', personaje, name='personaje'),
    path('staff/', staff, name='staff'),
    path('capitulo/', capitulo, name='capitulo'),
    path('franquicia/<str:slug_franquicia>/', franquicia, name='franquicia'),
    path('login/', login, name='login'),
    path('registro/', registro, name='registro'),
]
