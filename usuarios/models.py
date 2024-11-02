from django.db import models

class Usuario (models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    confirmar_senha = models.CharField(max_length=64)
    endereco = models.CharField(max_length=64)
    telefone = models.CharField(max_length=64)
    tipo_usuario = models.CharField(max_length=64)


    def __str__(self) -> str:
        return self.nome

