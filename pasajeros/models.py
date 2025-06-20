from django.db import models

# Create your models here.
class Pasajero(models.Model):
    Tipo_Documentos = [
        ('dni', 'DNI'),
        ('pasaporte', 'Pasaporte'),
        ('cedula', 'Cédula'),
    ]

    nombre = models.CharField(max_length=100)
    documento = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=20, choices=Tipo_Documentos)
    email = models.EmailField()
    telefono = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre