from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Livros
from .models import Emprestimo
from usuarios.models import Usuario


from django.urls import reverse

def home_admin(request):
    if request.session.get('usuario_adm'):
        livros_adm = Livros.objects.all()
        usuario = Usuario.objects.all()
        return render (request,'home_adm.html', {'livros_cadastrados':livros_adm, 'usuario':usuario})
        
    else: 
        return redirect('/auth/login/?status=2')

def home_leitor(request):
    if request.session.get('usuario_leitor'):
        return HttpResponse ('leitor')
    else: 
        return redirect('/auth/login/?status=2')
    
def cadastrar_livros (request):
   return render (request,'cadastrar_livros.html')

def ver_livros (request, id):
   livros = Livros.objects.get(id=id)
   emprestimos = Emprestimo.objects.filter(livro = livros)
   return render (request,'ver_livros.html',{'livros':livros,'emprestimos':emprestimos})

def home_leitor(request):
    if request.session.get('usuario_leitor'):
        livros_leitor = Livros.objects.all()
        return render (request,'home_leitor.html', {'livros_cadastrados':livros_leitor})

def ver_livros_leitor (request, id):
   livros = Livros.objects.get(id=id)
   return render (request,'ver_livros_leitor.html',{'livros':livros})

def validar_livros(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        autor = request.POST.get('autor')
        isbn = request.POST.get('isbn')
        editora = request.POST.get('editora')
        ano_publicacao = request.POST.get('ano_publicacao')
        descricao = request.POST.get('descricao')
        quantidade_total = request.POST.get('quantidade_total')
        quantidade_disponivel = request.POST.get('quantidade_disponivel')
        genero = request.POST.get('genero')

        livros_cadastro = Livros(nome=nome,autor=autor,isbn=isbn,editora=editora,ano_publicacao=ano_publicacao,genero=genero,descricao = descricao,quantidade_disponivel = quantidade_disponivel,quantidade_total= quantidade_total)
        livros_cadastro.save()
        return redirect('/livros/home/admin')

def deletar_livro(request,id):
    livro = Livros.objects.get(id=id)
    livro.delete()
    return redirect('home/admin')  

def cadastrar_emprestimo(request):
    pass