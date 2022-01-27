from django.urls import path
from .views import home, titulo, entrega, formato, personaje, capitulo, staff, franquicia, login, registro

urlpatterns = [
    path('<str:slug_titulo>/', titulo, name='titulo' ),
    path('', home, name='home' ),
    path('<str:formato>/', formato, name='formato' ),
    path('f/<str:slug_titulo>/<str:slug_entrega>/', entrega, name='entrega' ),
    path('personaje/<str:slug_personaje>/', personaje, name='personaje' ),
    path('staff', staff, name='staff' ),


    path('capitulo', capitulo, name='capitulo' ),
    path('franquicia', franquicia, name='franquicia' ),
    path('login', login, name='login' ),
    path('registro', registro, name='registro' ),
]