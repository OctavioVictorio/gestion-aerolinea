from django.contrib import admin

# Register your models here.
from reservas.models import (
    Boleto,
    Reserva,
)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('codigo_reserva', 'pasajero', 'vuelo', 'asiento', 'estado', 'fecha_reserva', 'precio',)
    search_fields = ('codigo_reserva', 'pasajero__nombre', 'vuelo__origen', 'vuelo__destino',)
    list_filter = ('estado', 'vuelo', 'pasajero',)


@admin.register(Boleto)
class BoletoAdmin(admin.ModelAdmin):
    list_display = ('codigo_barra', 'reserva', 'estado', 'fecha_emision')
    search_fields = ('codigo_barra', 'reserva__codigo_reserva')
    list_filter = ('estado', 'fecha_emision')