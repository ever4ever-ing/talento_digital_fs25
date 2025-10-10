from django.shortcuts import render
from django.http import HttpResponse
from .models import Cliente

def index(request):
    
    cliente = Cliente(nombre="Everardo Alvarado", email="ever@gmail.com", fecha_registro="2023-10-01 10:00:00")
    return render(request, "index_cliente.html", {"cliente": cliente})