from django.shortcuts import render, redirect
from django.http import HttpResponse

def home_admin(request):
    if request.session.get('usuario_adm'):
        return render (request,'home_adm.html')
    else: 
        return redirect('/auth/login/?status=2')

def home_leitor(request):
    if request.session.get('usuario_leitor'):
        return HttpResponse ('leitor')
    else: 
        return redirect('/auth/login/?status=2')
    
def cadastrar_livros (request):
   return render (request,'cadastrar_livros.html')