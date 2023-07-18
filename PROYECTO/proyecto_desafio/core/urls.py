from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path('', views.indexView, name = 'index'),
    path('articulos/', include('articulos.urls')),
    path('user/', include('usuarios.urls'))
]