from django.db import models

# Create your models here.

class Factura(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    # Número de la factura
    num = models.IntegerField(default=0) 
    # Año de la factura
    anio = models.DateField( auto_now=False, auto_now_add=False)
    # Fecha
    fecha_emision = models.DateField(auto_now=False, auto_now_add=False)
    # Nombre del cliente
    cliente_nombre = models.CharField(max_length=100)
    # Dirección del cliente
    cliente_direccion = models.CharField(max_length=300)

f = Factura(num=1, anio='2021', fecha_emision='2021', cliente_nombre='Yuriy', cliente_direccion='Toledo')
class LineaFactura(models.Model):
    id = models.AutoField(primary_key=True) 
    # Nombre del producto
    nombre_producto = models.ForeignKey(
        Factura, 
        blank=True,
        null=True,
        on_delete=models.PROTECT,)
    # Precio por unidad del producto
    precio_unitario = models.FloatField(default=0)
    # Total de unidades servidas
    unidades = models.IntegerField(default=1)
    # Método que devuelve el cálculo de precio unitario por el número de unidades
    def precio_real(self):
        return self.precio_unitario * self.unidades
    #