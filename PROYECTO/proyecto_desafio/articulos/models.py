

from django.db import models

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length= 250)

    def __str__(self):
        return self.nombre



class Articulos(models.Model):
    titulo = models.CharField(max_length = 250) 
    contenido = models.TextField()
    creacion = models.DateField(auto_now_add = True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL ,related_name = 'articulo_categoria', null = True )
   
    def __str__(self):
        return self.titulo
    
    def get_queryset(self):
       
       consulta_anterior = super().get_queryset()

       return consulta_anterior.order_by('creacion')




