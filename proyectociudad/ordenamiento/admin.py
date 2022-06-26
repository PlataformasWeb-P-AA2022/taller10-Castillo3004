from django.contrib import admin

# Importar la clase del modelo 

from ordenamiento.models import Barrio, Parroquia

class ParroquiaAdmin(admin.ModelAdmin):
    
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):
    
    list_display = ('nombre','nroViviendas','nroParques','nroEdificios', 'parroquia')
    raw_id_fields = ('parroquia',)

admin.site.register(Barrio, BarrioAdmin)