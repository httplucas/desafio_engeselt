from django.db import models
from datetime import date

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
    descricao = models.CharField(max_length=100, blank = True, null = True)
    emprestado = models.BooleanField(default = False)
    nome_emprestado = models.CharField(max_length=100, blank = True, null = True)
    data_emprestado = models.DateField(default =date.today, null = True) 
    tempo_duracao = models.DateField(blank = True, null = True)    
    genero_opcoes = [
        ('Fic', 'Ficção'),
        ('Rom', 'Romance'),
        ('Ter', 'Terror'),
        ('Aca', 'Ação'),
        ('Ave','Aventura')]
    genero = models.CharField(max_length=3, choices= genero_opcoes,blank=True, null = True)

    class Meta:
        verbose_name = 'Livros'

    def __str__(self):
        return self.nome
   


