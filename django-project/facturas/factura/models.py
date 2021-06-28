from django.db import models

# Create your models here.

class Factura(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    # Número de la factura
    num = models.PositiveIntegerField(default=0) 
    # Año de la factura
    anio = models.PositiveIntegerField(default=2000) 
    # Fecha
    fecha_emision = models.PositiveIntegerField(default=2000) 
    # Nombre del cliente
    cliente_nombre = models.CharField(max_length=100)
    # Dirección del cliente
    cliente_direccion = models.CharField(max_length=300)
    # Método para obtener todos los objetos de LineaFactura
    def lineas_factura(self):
        return LineaFactura.objects.filter(linea_factura=self)
    # Método para obtener la suma de todas las líneas de factura
    def precio_total(self):
        total = 0
        for lf in self.lineas_factura():
            total += lf.precio_real()
        return total
    # Método para obtener la suma total con IVA
    def total_iva(self):
        return self.precio_total() * 1.21

class LineaFactura(models.Model):
    id = models.AutoField(primary_key=True) 
    linea_factura = models.ForeignKey(
        Factura, 
        blank=True,
        null=True,
        on_delete=models.CASCADE,)
    # Utilizamos la opción de CASCADE para permitir el borrado de la factura completa.
    # Dado que con el PROTECT tendríamos que ir borrando una a una cada línea de factura antes de poder borrar la factura.
    # Nombre del producto
    nombre_producto = models.CharField(default = "",max_length=100)
    # Precio por unidad del producto
    precio_unitario = models.FloatField(default=0)
    # Total de unidades servidas
    unidades = models.IntegerField(default=1)
    # Método que devuelve el cálculo de precio unitario por el número de unidades
    def precio_real(self):
        return self.precio_unitario * self.unidades
    #