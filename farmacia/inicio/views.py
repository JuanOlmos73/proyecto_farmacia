from django.shortcuts import render

# Create your views here.
def principal (request):
    return render (request, "inicio/principal.html")

def registrar_farmacos(request):
    return render (request,"inicio/reg_farmacos.html")

def salida_farmacos(request):
    return render (request, "inicio/salida_farmacos.html")

def inventarios (request):
    return render (request,"inicio/inventario.html")