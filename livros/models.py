from django.db import models

#Criar banco de dados do livro
class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    isbn = models.CharField(max_length=100)
    editora = models.CharField(max_length=30)
    ano_publicacao = models.DateField()
    genero = models.CharField(max_length=30)
    quantidade_total = models.IntegerField()
    quantidade_disponivel = models.IntegerField()
    descricao = models.CharField(max_length=100)
    

#Criar banco de dados do emprestimo
class Emprestimo(models.Model):
    emprestado = models.BooleanField(default=False)
    nome_emprestado = models.CharField(max_length=100)
    data_emprestado = models.DateTimeField()
    data_devolucao = models.DateTimeField()
    tempo_duracao = models.DateField()
