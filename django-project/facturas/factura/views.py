from django.shortcuts import render
from django.http import HttpResponse
from .models import Factura, LineaFactura

# Create your views here.

def hola(request):
    return HttpResponse("Hola, Mundo")

def detalle(request, pk):
    fc = Factura.objects.get(id=pk)
    return render(request, 'factura/main.html', {
        "fc": fc, 
    })

def listado_factura(request):
    factura = Factura.objects.all()
    linea_factura = LineaFactura.objects.all()
    return render(request, 'factura/listado.html', {
        'factura': factura,
        'linea_factura': linea_factura 
    })