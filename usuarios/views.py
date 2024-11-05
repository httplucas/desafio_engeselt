from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Usuario
from hashlib import sha256

def login(request):
    status = request.GET.get('status')
    return render (request, 'login.html',{'status': status})

def cadastro(request):
    status = request.GET.get('status')
    return render (request,'cadastro.html',{'status': status})

def valida_cadastro(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    confirmar_senha = request.POST.get('confirmar_senha')
    endereco = request.POST.get('endereco')
    telefone = request.POST.get('telefone')
    tipo_usuario = request.POST.get('tipo_usuario')

#Validação do email
    usuario = Usuario.objects.filter(email = email)

    if len(nome.strip()) == 0 or len(email.strip()) == 0: 
        return redirect ('/auth/cadastro/?status=1')
    if len (usuario) > 0:
        return redirect ('/auth/cadastro/?status=2')

#Validação da senha
    if senha != confirmar_senha:
        return redirect ('/auth/cadastro/?status=3')
    try:
        senha = sha256(senha.encode()).hexdigest() #codificar minha senha
        usuario = Usuario(nome = nome, senha = senha, endereco = endereco, tipo_usuario = tipo_usuario, email = email, telefone = telefone)
        usuario.save()
        return redirect ('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=3')
    
def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    senha = sha256(senha.encode()).hexdigest()

    # Busca pelo usuário com email e senha
    usuario = Usuario.objects.filter(email=email, senha=senha).first()

    if usuario is None:
        return redirect('/auth/login/?status=1')  #Se email ou senha estiverem errados, retorna mensagem de erro

    # Usuário encontrado

    # Verifica o tipo de usuário
    if usuario.tipo_usuario == 'Administrador':
        request.session['usuario_adm'] = usuario.id 
        return redirect('/livros/home/admin')  # administrador
    
    elif usuario.tipo_usuario == 'Leitor':
        request.session['usuario_leitor'] = usuario.id 
        return redirect('/livros/home/leitor')  # leitor

    # Se nenhum dos casos se aplicar, redireciona para login
    return redirect('/auth/login/?status=1')

def sair(request):
    request.session.flush()
    return redirect('/auth/login')

def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    return render (request,'listar_usuarios.html',{'usuarios':usuarios})