from django.shortcuts import render

from django.views.generic.edit import CreateView

from django.contrib.auth.models import User

from django.contrib.auth.forms import  UserCreationForm

from django.urls import reverse
# Create your views here.

class RegistroView(CreateView):
    model = User
    template_name = 'usuarios/registro.html'
    form_class = UserCreationForm

    def get_success_url(self):
        return reverse('index')
        




