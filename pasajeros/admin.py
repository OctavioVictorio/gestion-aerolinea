from django.contrib import admin

# Register your models here.
from pasajeros.models import (
    Pasajero,
)

@admin.register(Pasajero)
class PasajeroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'documento', 'tipo_documento', 'email', 'telefono', 'fecha_nacimiento')
    list_filter = ('nombre','documento',)
    search_fields = ('nombre', 'documento', 'email',)