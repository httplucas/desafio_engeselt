from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario
def login(request):
    return HttpResponse ('login')

def cadastro(request):
    return render (request,'cadastro.html')

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    endereco = request.POST.get('endereco')
    telefone = request.POST.get('telefone')
    tipo_usuario = request.POST.get('dropdown')

    return HttpResponse (f"{nome} {senha} {tipo_usuario}")