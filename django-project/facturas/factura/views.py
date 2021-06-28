from django.shortcuts import render
from django.http import HttpResponse
from .models import Factura, LineaFactura

# Create your views here.

def main(request):
    return render(request, 'factura/main.html')

def detalle(request, pk):
    fc = Factura.objects.get(id=pk)
    linea_factura = LineaFactura.objects.all()
    return render(request, 'factura/detalle.html', {
        'fc': fc, 
        'linea_factura': linea_factura,
    })

def listado_factura(request):
    factura = Factura.objects.all()
    linea_factura = LineaFactura.objects.all()
    return render(request, 'factura/listado.html', {
        'factura': factura,
        'linea_factura': linea_factura, 
    })