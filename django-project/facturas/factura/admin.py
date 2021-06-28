from django.contrib import admin

# Register your models here.

from .models import Factura, LineaFactura

class FacturaAdmin(admin.ModelAdmin):
    list_display = ('num', 'anio', 'fecha_emision', 'cliente_nombre', 'cliente_direccion')


admin.site.register(Factura, FacturaAdmin)


class LineaFacturaAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'precio_unitario')

admin.site.register(LineaFactura, LineaFacturaAdmin)
