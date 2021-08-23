from django.shortcuts import get_object_or_404, render
from .models import medicamentos
from .models import salida_medicamento
from .forms import Medicamentoforms
from django.contrib import messages
from .forms import editarforms
from .forms import salidaFarmacoforms
'''from .models import salida_medicamento
from .forms import salidaFarmacoforms'''

#funcion  del estock que me regresa todos los objetos de la base de datos en inventario
def stock(request):
      medi=medicamentos.objects.all()
      return render(request, "registrofarmacia/inventario.html",{'medi': medi})
#fin de la funcion

#funcion que visualiza la view de la pagina de registro de los medicamentos
def regitrarfarmacia(request):
    return render (request,"registrofarmacia/reg_farmacos.html")
#fin de la funcion view de registro de los medicamentos

#funcion de registrar. Registra lo que alla en los campos del forumulario de la view de reg_farmacos y despues los guarda para 
# de esta manera imprimir la informacion
def registrar(request):
    if request.method == 'POST':
        form=Medicamentoforms(request.POST,request.FILES)
        if form.is_valid():
            clave=request.POST['clave']
            nombre=request.POST['nombre']
            cantidad=request.POST['cantidad']
            fecha_de_caducidad=request.POST['fecha_de_caducidad']
            descripcion=request.POST['descripcion']
            imagen=request.FILES ['imagen']
            disponibilidad=request.POST['disponibilidad']
            form=medicamentos (clave=clave, nombre=nombre, cantidad=cantidad, fecha_de_caducidad=fecha_de_caducidad, descripcion=descripcion, imagen=imagen, disponibilidad=disponibilidad)
            form.save()
            medi=medicamentos.objects.all()
            return render(request,'registrofarmacia/inventario.html',{'medi': medi})
        else:
            messages.error(request,"Error al procesar el formulario")
    form=Medicamentoforms()
    return render (request,'registrofarmacia/reg_farmacos.html',{'form':form})
#fin de la funcion rigistrar

#funcion principa_registros esta funcion nos ayuda a visualizar la vista de principal como tambien obtiene por medio de un filtro los medicamentos que estan por agotarse
def principal_registros(request):
    medi=medicamentos.objects.filter(cantidad__lte=5)
    return render(request, "registrofarmacia/principal.html",{'medi':medi})
#fin de la funcion principal

#funcion salida_farmacos nos permite visualizar la view de salida 
def salida_farmacos(request):
    medi=medicamentos.objects.all()
    return render(request,"registrofarmacia/salida_farmacos.html",{'medi':medi})
#fin de la funcion de salida de farmacos

#funcion reabastecer esta funcion nos ayuda a visualizar la view de reabastecer.html
def rellenar(request, id):
    medis=medicamentos.objects.get(id=id)
    return render(request,"registrofarmacia/reabastecer.html",{'medi':medis})

#funcion editar farmaco esta funcion nos permitira reabastecer los medicamentos
def editar(request, id):
    medis=get_object_or_404(medicamentos, id=id)
    canti_actual=medis.cantidad
    form1= editarforms(request.POST, instance=medis)
    if form1.is_valid():
        '''la variable nuevo es una copia del formulario almacenado de forma temporal'''
        nuevo=form1.save(commit=False)
        '''Se extrae el valor actial del formulario y se suma a al dato ya existente en la base de datos'''
        cantidad=form1.data['cantidad']
        nuevacantidad=int(cantidad)+int(canti_actual)
        '''Actualizamos la existencia guardada de forma temporal con la suma'''
        nuevo.cantidad=nuevacantidad
        '''se aplica el guardado con los cambios de existencia'''
        nuevo.save()
        medis=medicamentos.objects.all()
        return render(request, "registrofarmacia/inventario.html",{'medi': medis})
    else:
        messages.error(request,"Error al procesar los datos")

    form=editarforms()
    return render(request,'registrofarmacia/principal.html',{'form':form})
#fin de la funcuin editar

def salidafarmaco(request):
    if request.method == 'POST':
    
        form2=salidaFarmacoforms(request.POST)
        if form2.is_valid():
            form2.save()
        cantidad_suministro=form2.data['cantidad_suministrada']
        medicamento = request.POST['medicamento']
        print(cantidad_suministro)
        
        medis=get_object_or_404(medicamentos, id=medicamento)
        cantidad_actual=medis.cantidad
        nuevacantidad=int(cantidad_actual)-int(cantidad_suministro)
        medis.cantidad = nuevacantidad
        medis.save()
        print(cantidad_actual)
        medis=medicamentos.objects.all()
        return render(request, "registrofarmacia/inventario.html",{'medi': medis})
    else:
        messages.error(request,"Error al procesar los datos")

    form=salidaFarmacoforms()
    return render(request,'registrofarmacia/salida_farmacos.html',{'form':form})

