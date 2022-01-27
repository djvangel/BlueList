from django.contrib import admin
from .models import *
# Register your models here.

from django_summernote.admin import SummernoteModelAdmin

# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'



admin.site.register(Franquicia, SomeModelAdmin)
admin.site.register(Titulo, SomeModelAdmin)
admin.site.register(Personaje, SomeModelAdmin)
admin.site.register(Staff, SomeModelAdmin)
admin.site.register(Entrega, SomeModelAdmin)