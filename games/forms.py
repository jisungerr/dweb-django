from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm

from games.models import *


class CriarJogo(forms.ModelForm):

    class Avaliacao:
        AVALIACAO = (
            (1, 'Muito bom'),
            (2, 'Bom'),
            (3, 'Mediano'),
            (4, 'Ruim'),
            (5, 'Péssimo')
        )

    genero = forms.ModelMultipleChoiceField(
        queryset=Genero.objects.all(), widget=forms.CheckboxSelectMultiple)
    plataforma = forms.ModelMultipleChoiceField(
        queryset=Plataforma.objects.all(), widget=forms.CheckboxSelectMultiple)
    avaliacao = forms.ChoiceField(choices=Avaliacao.AVALIACAO)
    capa = forms.ImageField()
    desenvolvedor = forms.ModelMultipleChoiceField(
        queryset=Desenvolvedor.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Jogos
        fields = ['nome', 'data', 'genero', 'enredo', 'usuario',
                  'avaliacao', 'critica', 'plataforma', 'desenvolvedor', 'capa']
        widgets = {
            'data': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control',
                       'type': 'date'
                       }
            )}


class UserForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class LoginForm(AuthenticationForm):
    class Meta:
        widgets = {'password': forms.PasswordInput(attrs={'id': 'inputPassword', 'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'id': 'inputEmail', 'class': 'form-control'})}
