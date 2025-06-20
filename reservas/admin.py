from django.contrib import admin

# Register your models here.
from reservas.models import (
    Reserva,
)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('codigo_reserva', 'pasajero', 'vuelo', 'asiento', 'estado', 'fecha_reserva', 'precio',)
    search_fields = ('codigo_reserva', 'pasajero__nombre', 'vuelo__origen', 'vuelo__destino',)
    list_filter = ('estado', 'vuelo', 'pasajero',)