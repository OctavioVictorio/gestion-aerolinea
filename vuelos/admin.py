from django.contrib import admin

# Register your models here.
from vuelos.models import (
    Vuelo,
)


@admin.register(Vuelo)
class VueloAdmin(admin.ModelAdmin):
    list_display = ('origen', 'destino', 'fecha_salida', 'precio_base', 'estado')
    list_filter = ('origen', 'destino', 'estado')
    search_fields = ('origen', 'destino')
