from django.db import models

# Create your models here.
class Vuelo(models.Model):
    ESTADO_VUELO = [
        ('programado', 'Programado'),
        ('en_vuelo', 'En vuelo'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ]

    avion = models.ForeignKey('flota.Avion', on_delete=models.CASCADE)
    origen = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    fecha_salida = models.DateTimeField()
    fecha_llegada = models.DateTimeField()
    duracion = models.DurationField()
    estado = models.CharField(max_length=20, choices=ESTADO_VUELO)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Vuelo {self.origen} → {self.destino} - {self.fecha_salida.strftime('%Y-%m-%d %H:%M')}"
