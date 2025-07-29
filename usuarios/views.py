from django.shortcuts import render, redirect
from django.contrib import messages #Módulo de mensagens
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django #as - use como


def cadastro(request):
    if request.method == "POST": #Se o botão de criar conta for clicado, renderiza pag login

        #A variável vai receber o que o usuário preencher, se for get ou post
        username = request.POST.get('user') #O que está dentro do parêntese é o 'name' do template
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')

        if not username.strip():
            messages.error(request, 'Preencha o campo de usuário corretamente')
            return redirect('cadastro')
        
        if not email.strip():
            messages.error(request, 'Preencha o campo de e-mail corretamente')
            return redirect('cadastro')

        if senha != senha2:
            messages.error(request, 'As senhas devem ser iguais')
            return redirect('cadastro')
        
        if len(senha) < 6:
            messages.error(request, 'As senhas devem ter, no mínimo, 8 caracteres')
            return redirect('cadastro')
        
        
        if User.objects.filter(email=email).exists(): #Verificando de o usuário já existe
            messages.error(request, 'Usuário já cadastrado')
            return redirect('login')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um perfil com esse nome de usuário')
            return redirect('login')
        
        user = User.objects.create_user(username=username, email=email, password=senha) #Criando um usuário
        user.save()

        messages.success(request, 'Usuário criado com sucesso')
        print('cadastrou')

        return redirect('login')
    
    else:
        return render(request, 'usuarios/cadastro.html')


def fazer_login(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        senha = request.POST.get('password')
        
        user = authenticate(request, username=user, password=senha)

        if user:
            login_django(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Credenciais inválidas')
            return redirect('login')
        
    else:
        return render(request, 'usuarios/login.html')


def logout(request):
    auth.logout(request) 
    return render(request, 'usuarios/login.html')


