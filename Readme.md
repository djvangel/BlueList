# Lista de caracteristicas

- [x] entorno virtual y variables de entorno
- [x] estructura de archivos static / templates y apps
    - [x] configuracion de apps alojadas en una carpeta
    - [x] configuracion de los archivos static
    - [x] configuracion de app core y las paginas estaticas
    - [x] configuracion de los templates
        - pagina principal
        - navbar
        - footer
        - contacto
    - [x] Views de paginas principalas
- [x] Pagina de detalles de titulo
- [x] Pagina de capitulo
- [x] estructura de base de datos
- [x] Estructura de relaciones
- [ ] Agregar descripcion a los titulos
- [ ] Agregar Franquicias 

# Fase 1 

## diseño de base de datos

## __Agrego Variables globales__
### 1.- archivo  `context_processors.py`
[1](1)
```python
from .models import Formato
def menu_categories(request): 
    categories = Formato
    return {'menu_categories': categories} 

```
### 2.- Ahora puedo llamar `Formato` en cualquer componente

la view de la correspondiente url:
```python
def formato(request, formato):
    titulos = Titulo.objects.filter(formato = formato ).all()
    ctx = {"titulos": titulos}
    return render(request, 'core/home.html', ctx)

```

```html
{% for i in menu_categories %}
    <a class="m-2 btn btn-sm btn-outline-secondary" href="{% url 'formato' i.value %}">{{ i.value }}</a>
{% endfor %}
```

## Agrego todas las views







**Mas adelante repetire este proseso con las variables que deseo usar en los deferentes componentes**