# Generated by Django 4.2.3 on 2023-07-12 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, unique=True)),
                ('activo', models.BooleanField(default=True)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=250)),
                ('bajada', models.CharField(max_length=600)),
                ('contenido', models.TextField()),
                ('publicado', models.BooleanField(default=False)),
                ('creacion', models.DateField(auto_now_add=True)),
                ('actualizacion', models.DateField(auto_now_add=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articulos.categoria')),
                ('etiqueta', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='articulos.etiqueta')),
            ],
        ),
    ]