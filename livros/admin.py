from django.contrib import admin
from .models import Livros , Categoria , Emprestimo

# Registrando minha model Livros
admin.site.register(Livros)
admin.site.register(Categoria)
admin.site.register(Emprestimo)
