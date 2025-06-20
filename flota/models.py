from django.db import models

# Create your models here.
class Avion (models.Model):
    modelo = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    filas = models.PositiveIntegerField()
    columnas = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.modelo} {self.capacidad} asientos'
    

class Asiento (models.Model):
    TIPO_ASIENTO = [
        ('economico', 'Económico'),
        ('business', 'Business'),
        ('primera', 'Primera clase'),
    ]

    ESTADO_ASIENTO = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),
        ('ocupado', 'Ocupado'),
    ]


    avion = models.ForeignKey(Avion, on_delete=models.CASCADE)
    numero = models.PositiveIntegerField()
    fila = models.PositiveIntegerField()
    columna = models.PositiveIntegerField()
    tipo = models.CharField(max_length=20, choices=TIPO_ASIENTO)
    estado = models.CharField(max_length=20, choices=ESTADO_ASIENTO, default='disponible')


    def __str__(self):
        return f"Asiento {self.numero} - Fila {self.fila} Col {self.columna} ({self.tipo}) - {self.estado}"
