from django.db import models

class Vehiculo(models.Model):
    MARCAS = [
        ('Fiat', 'Fiat'),
        ('Chevrolet', 'Chevrolet'),
        ('Ford', 'Ford'),
        ('Toyota', 'Toyota'),
    ]
    
    CATEGORIAS = [
        ('Particular', 'Particular'),
        ('Transporte', 'Transporte'),
        ('Carga', 'Carga'),
    ]

    marca = models.CharField(max_length=20, choices=MARCAS, default='Ford')
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50, unique=True)
    serial_motor = models.CharField(max_length=50, unique=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='Particular')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    condicion_precio = models.CharField(max_length=10, blank=True)  # Nuevo campo para la condición de precio

    def save(self, *args, **kwargs):
        # Asigna automáticamente la condición de precio basado en el valor de `precio`
        if self.precio <= 10000:
            self.condicion_precio = "Bajo"
        elif self.precio <= 30000:
            self.condicion_precio = "Medio"
        else:
            self.condicion_precio = "Alto"
        print(f"Precio: {self.precio}, Condición de precio: {self.condicion_precio}")   
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.marca} {self.modelo}"




