from django.shortcuts import render

from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Articulos, Categoria

from .forms import CrearArticuloForm

from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#ctx = {'articulos' : Articulos.objects.all()}

class VerArticulos(ListView):
    model = Articulos
    template_name = 'articulos/articulos.html'
    context_object_name = 'articulos'

class Publicar(CreateView, LoginRequiredMixin):
    model = Articulos
    template_name = 'articulos/publicar.html' 
    form_class = CrearArticuloForm

    def get_success_url(self):
        return reverse('articulos:articulos')
    



class EditarPost(UpdateView, LoginRequiredMixin):
    model = Articulos
    template_name = 'articulos/editar_articulo.html'

    form_class = CrearArticuloForm
    
    def get_success_url(self):
        return reverse('articulos:articulos')
    

class EliminarPost(DeleteView):
    template_name = 'articulos/eliminar_articulo.html'

    model = Articulos
    
    def get_success_url(self):
        return reverse('articulos:articulos')
    
class VerCategorias(ListView):
    model = Categoria
    template_name = 'articulos/categorias.html'
    context_object_name = 'categoria'


def contacto(request):
    return render(request, 'articulos/contacto.html')

