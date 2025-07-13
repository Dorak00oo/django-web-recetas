from django.db import models


class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen_principal = models.ImageField(upload_to='recetas/')

    def __str__(self):
        return self.titulo


class IngredientePadre(models.Model):
    receta = models.ForeignKey(Receta, related_name='ingredientes_padre', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class IngredienteHijo(models.Model):
    padre = models.ForeignKey(IngredientePadre, related_name='ingredientes_hijo', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.padre.nombre} - {self.nombre}"


class Paso(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE, related_name='pasos')
    titulo = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='pasos/', blank=True, null=True)
    orden = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['orden']

    def __str__(self):
        return f"Paso {self.orden}: {self.titulo or 'Sin título'}"