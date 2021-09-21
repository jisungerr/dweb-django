from django.db import models
from django.contrib.auth.models import AbstractUser, User


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'


class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Genero(models.Model):
    tipo = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.tipo


class Desenvolvedor(models.Model):
    nome = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.nome


class Jogos(models.Model):
    AVALIACAO = (
        (1, 'Muito bom'),
        (2, 'Bom'),
        (3, 'Mediano'),
        (4, 'Ruim'),
        (5, 'Péssimo')
    )

    nome = models.CharField(max_length=100)
    data = models.DateField()
    genero = models.ManyToManyField(Genero)
    enredo = models.TextField()
    desenvolvedor = models.ManyToManyField(Desenvolvedor)
    avaliacao = models.IntegerField(choices=AVALIACAO)
    critica = models.TextField()
    plataforma = models.ManyToManyField(Plataforma)
    capa = models.ImageField(upload_to='images')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    @property
    def get_avaliacao(self):
        if self.avaliacao == 1:
            return "Muito bom"
        elif self.avaliacao == 2:
            return "Bom"
        elif self.avaliacao == 3:
            return "Mediano"
        elif self.avaliacao == 4:
            return "Ruim"
        else:
            return "Pessimo"

