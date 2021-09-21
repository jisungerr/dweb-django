from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from . import models
from .forms import CriarJogo, LoginForm
from django.urls import reverse_lazy

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.views.generic.edit import DeleteView, UpdateView, CreateView

from django.contrib.auth.views import LoginView

from .forms import UserForm


class Home(ListView):
    model = models.Jogos
    template_name = 'home.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            queryset = models.Jogos.objects.all().filter(usuario=self.request.user)
            return queryset
        return


class ViewJogos(DetailView):
    model = models.Jogos
    template_name = 'jogos.html'


class DeletarJogo(DeleteView):
    model = models.Jogos
    success_url = reverse_lazy('home')


class EditarJogo(UpdateView):
    model = models.Jogos
    form_class = CriarJogo
    success_url = reverse_lazy('home')


class CreateJogo(CreateView):
    model = models.Jogos
    form_class = CriarJogo
    template_name = 'games/cadastrojogo.html'
    success_url = reverse_lazy('home')


class Login(LoginView):
    template_name = 'registration/login.html'
    authentication_form = LoginForm


class AccountCreate(CreateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'games/cadastrouser.html'
    success_url = reverse_lazy('login')


class AccountEdit(UpdateView):
    model = get_user_model()
    form_class = UserForm
    template_name = 'games/editar_conta.html'
    success_url = reverse_lazy('index')

    login_url = '/login/'


class AccountDelete(DeleteView):
    model = get_user_model()
    success_url = reverse_lazy('index')
    template_name = 'games/jogos_confirm_delete.html'
    login_url = '/login/'
