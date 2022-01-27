from .models import Formato

def menu_categories(request): # NOMBRE DE LA FUNCION DEBEN SER IGUALES
    categories = Formato

    return {'menu_categories': categories} # NOMBRE DEL OBJETO LLAMABLE DEBEN SER IGUALES