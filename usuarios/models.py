from django.db import models

class Usuario (models.Model):
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    senha = models.CharField(max_length=64)
    confirmar_senha = models.CharField(max_length=64)
    endereco = models.CharField(max_length=64, blank = True, null = True)
    telefone = models.CharField(max_length=64, blank = True, null = True)
    tipo_usuario = [
        ('Administrador', 'Administrador'),
        ('Leitor', 'Leitor'),
]
    tipo_usuario = models.CharField(max_length=50, choices= tipo_usuario,blank=True, null = True)

    def __str__(self) -> str:
        return self.nome

