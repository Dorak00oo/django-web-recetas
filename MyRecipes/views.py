from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Receta


def index(request):
    recetas = Receta.objects.all()
    return render(request, 'index.html', {'recetas': recetas})


def receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    ingredientes_padre = receta.ingredientes_padre.all()
    pasos = receta.pasos.all()
    
    return render(request, 'receta.html', {
        'receta': receta,
        'ingredientes_padre': ingredientes_padre,
        'pasos': pasos,
    })
