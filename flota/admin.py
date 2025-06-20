from django.contrib import admin

# Register your models here.
from flota.models import (
    Asiento,
    Avion,
)


@admin.register(Avion)
class AvionAdmin(admin.ModelAdmin):
    list_display = ('modelo', 'capacidad', 'filas', 'columnas')
    search_fields = ('modelo',)
    list_filter = ('modelo',)


@admin.register(Asiento)
class AsientoAdmin(admin.ModelAdmin):
    list_display = ('avion', 'numero', 'fila', 'columna', 'tipo', 'estado')
    search_fields = ('numero', 'fila', 'columna', 'tipo')
    list_filter = ('avion', 'tipo', 'estado')