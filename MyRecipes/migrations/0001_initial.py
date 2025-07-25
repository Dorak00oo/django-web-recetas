# Generated by Django 5.2.4 on 2025-07-12 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IngredientePadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen_principal', models.ImageField(upload_to='recetas/')),
            ],
        ),
        migrations.CreateModel(
            name='IngredienteHijo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('padre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes_hijo', to='MyRecipes.ingredientepadre')),
            ],
        ),
        migrations.CreateModel(
            name='Paso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='pasos/')),
                ('orden', models.PositiveIntegerField(default=1)),
                ('receta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasos', to='MyRecipes.receta')),
            ],
            options={
                'ordering': ['orden'],
            },
        ),
        migrations.AddField(
            model_name='ingredientepadre',
            name='receta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredientes_padre', to='MyRecipes.receta'),
        ),
    ]
