from django.contrib import admin

import nested_admin
from .models import Receta, IngredientePadre, IngredienteHijo, Paso

class IngredienteHijoInline(nested_admin.NestedTabularInline):
    model = IngredienteHijo
    extra = 0

class IngredientePadreInline(nested_admin.NestedTabularInline):
    model = IngredientePadre
    inlines = [IngredienteHijoInline]
    extra = 1

class PasoInline(nested_admin.NestedTabularInline):
    model = Paso
    extra = 1

class RecetaAdmin(nested_admin.NestedModelAdmin):
    inlines = [IngredientePadreInline, PasoInline]

admin.site.register(Receta, RecetaAdmin)
