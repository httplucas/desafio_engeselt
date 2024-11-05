from django.db import models
from datetime import date
from usuarios.models import Usuario
#Categoria do livro
class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    def __str__(self): 
        return self.nome 
# banco de dados do livro
class Livros(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    isbn = models.CharField(max_length=100)
    editora = models.CharField(max_length=30)
    ano_publicacao = models.CharField(max_length=15)
    genero = models.CharField(max_length=30,blank = True, null = True)
    quantidade_total = models.CharField(max_length=15)
    quantidade_disponivel = models.CharField(max_length=15)
    descricao = models.TextField(max_length=500)
    emprestado = models.BooleanField(default = False)
    data_cadastro = models.DateField(default = date.today, null = True)  
    tempo_duracao = models.DateField(blank = True, null = True)    
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING,blank = True, null = True)
    genero = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Livros'

    def __str__(self): #Aparecer o titulo dos livros no banco
        return self.nome 
   
   #Emprestimo
class Emprestimo(models.Model):
      nome_emprestado = models.ForeignKey(Usuario,on_delete=models.DO_NOTHING)
      data_emprestado = models.DateField(default = date.today, null = True)
      data_devolucao = models.DateField(max_length=100, blank = True, null = True)
      tempo_duracao = models.DateField(max_length=100, blank = True, null = True)
      livro = models.ForeignKey(Livros,on_delete=models.DO_NOTHING)
      def temp_duracao(self):
        return self.data_emprestado - self.data_devolucao

def __str__(self): #Aparecer o titulo dos livros no banco
        return self.nome
