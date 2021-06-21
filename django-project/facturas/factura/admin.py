from django.contrib import admin

# Register your models here.

from .models import Factura, LineaFactura

class FacturaAdmin(admin.ModelAdmin):
    search_fields = (
        'id',
        'num',
        'anio',
        'fecha_emision',
        'cliente_nombre',
        'cliente_direccion',
    )
    list_display = ('id', 'num', 'anio', 'fecha_emision', 'cliente_nombre', 'cliente_direccion')


admin.site.register(Factura, FacturaAdmin)


class LineaFacturaAdmin(admin.ModelAdmin):
    search_fields = (
        'id',
        'nombre_producto',
        'precio_unitario',
        'unidades',
    )
    list_display = ('id','nombre_producto', 'precio_unitario', 'unidades')

admin.site.register(LineaFactura, LineaFacturaAdmin)
