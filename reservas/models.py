from django.db import models

# Create your models here.
class Reserva(models.Model):
    Estado = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('cancelada', 'Cancelada'),
    ]
    
    vuelo = models.ForeignKey('vuelos.Vuelo', on_delete=models.CASCADE)
    pasajero = models.ForeignKey('pasajeros.Pasajero', on_delete=models.CASCADE)
    asiento = models.ForeignKey('flota.Asiento', on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=Estado)
    fecha_reserva = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_reserva = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Reserva {self.codigo_reserva} - {self.pasajero} en vuelo {self.vuelo}"
