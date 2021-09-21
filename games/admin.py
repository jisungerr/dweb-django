from django.contrib import admin
from . import models

admin.site.register(models.Usuario)
admin.site.register(models.Desenvolvedor)
admin.site.register(models.Jogos)
admin.site.register(models.Genero)
admin.site.register(models.Plataforma)
