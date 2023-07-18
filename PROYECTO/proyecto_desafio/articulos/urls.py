from django.urls import path

from .views import VerArticulos, Publicar, EditarPost, EliminarPost, VerCategorias, contacto

app_name = 'articulos'

urlpatterns = [
    path('articulos/', VerArticulos.as_view(), name = 'articulos'),
    path('publicar/', Publicar.as_view(), name= 'publicar'),
    path('editar-articulo/<int:pk>', EditarPost.as_view(), name = 'editar_post'),
    path('eliminar-articulo/<int:pk>', EliminarPost.as_view(), name = 'eliminar_post'),
    path('categorias/', VerCategorias.as_view(), name = 'categorias'),
    path('contacto/', contacto, name = 'contacto')
]