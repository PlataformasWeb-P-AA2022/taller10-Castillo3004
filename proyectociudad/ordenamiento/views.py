from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# Create your views here.
from ordenamiento.models import *

from ordenamiento.forms import *

# Vista que lista las parroquias y sus barrios
def index (request):
    
    parroquias = Parroquia.objects.all()

    informacion_template = {'parroquias': parroquias, 'numero_parroquias': len(parroquias)}
    return render(request, 'index.html', informacion_template)


# Vista que lista los barrios
def lista_barrios (request):
    
    barrios = Barrio.objects.all()

    informacion_template = {'barrios': barrios, 'numero_barrios': len(barrios)}
    return render(request, 'lista_barrios.html', informacion_template)


# Vista que obtiene los barrios
def obtener_barrio(request, id):
    
    barrio = Barrio.objects.get(pk=id)

    informacion_template = {'barrio': barrio}
    
    return render(request, 'obtener_barrio.html', informacion_template)

# Vista que crea una parroquia
def crear_parroquia(request):
    """
    """

    if request.method=='POST':
        formulario = ParroquiaForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearParroquia.html', diccionario)


# Vista que crea un Barrio
def crear_barrio(request):
    """
    """

    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crearBarrio.html', diccionario)


# Vista que crea un Barrio de una Parroquia
def crear_barrio_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioParroquiaForm(parroquia, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioParroquiaForm(parroquia)
    diccionario = {'formulario': formulario, 'parroquia': parroquia}

    return render(request, 'crearBarrioParroquia.html', diccionario)


# Vista que edita una parroquia
def editar_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    if request.method=='POST':
        formulario = ParroquiaForm(request.POST, instance=parroquia)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = ParroquiaForm(instance=parroquia)
    diccionario = {'formulario': formulario}

    return render(request, 'editarParroquia.html', diccionario)


# Vista que edita un barrio
def editar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarBarrio.html', diccionario)


# Elimina una Parroquia
def eliminar_parroquia(request, id):
    """
    """
    parroquia = Parroquia.objects.get(pk=id)
    parroquia.delete()
    return redirect(index)


# Elimina un Barrio
def eliminar_barrio(request, id):
    """
    """
    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)
