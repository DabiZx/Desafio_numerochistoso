# Generated by Django 4.2.3 on 2023-07-18 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0002_articulos_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articulos',
            name='actualizacion',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='bajada',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='etiqueta',
        ),
        migrations.RemoveField(
            model_name='articulos',
            name='publicado',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Etiqueta',
        ),
    ]
