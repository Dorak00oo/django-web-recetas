# migrate_images_to_cloudinary.py

import os
import django
import cloudinary.uploader

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
django.setup()

from MyRecipes.models import Receta, Paso

def subir_y_actualizar_imagen(obj, campo, carpeta):
    imagen_local = getattr(obj, campo)
    if not imagen_local:
        return
    response = cloudinary.uploader.upload(imagen_local.path, folder=f"recetas_django/{carpeta}/")
    imagen_url = response["secure_url"]
    setattr(obj, campo, imagen_url)
    obj.save()
    print(f"✓ Subida: {imagen_url}")

for receta in Receta.objects.all():
    subir_y_actualizar_imagen(receta, "imagen_principal", "recetas")

for paso in Paso.objects.all():
    subir_y_actualizar_imagen(paso, "imagen", "pasos")

print("✅ Migración completa.")
