from django.shortcuts import render, redirect
from django.contrib.auth.models import User #Modelo de usuário do django
from django.contrib.auth import authenticate, login
from django.contrib import messages #Módulo de mensagens
from django.contrib import auth 

def cadastro(request):
    if request.method == "POST": #Se o botão de criar conta for clicado
        #A variável vai receber o que o usuário preencher, se for get ou post
        username = request.POST.get('user').lower() #O que está dentro do parêntese é o 'name' do template
        email = request.POST.get('email').lower()
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')

        #Realizando verificações
        if not username.strip():
            messages.error(request, 'Preencha o campo de usuário corretamente') #Mensagem de erro com o módulo messages
            return redirect('cadastro')
        
        if not email.strip():
            messages.error(request, 'Preencha o campo de e-mail corretamente')
            return redirect('cadastro')

        if senha != senha2:
            messages.error(request, 'As senhas devem ser iguais')
            return redirect('cadastro')
        
        if len(senha) < 8:
            messages.error(request, 'As senhas devem ter, no mínimo, 8 caracteres')
            return redirect('cadastro')
        
        #Verificando senão existe nenhum objeto User com o e-mail fornecido
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('login')
        
        #Verificando senão existe nenhum objeto User com o username fornecido
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Já existe um perfil com esse nome de usuário')
            return redirect('login')
        
        #Se ele não entrar em nenhum if, user recebe a instanciação do objeto, usuário é criado
        user = User.objects.create_user(username=username, email=email, password=senha) 
        user.save()

        messages.success(request, 'Usuário criado com sucesso')

        return redirect('login')
    
    else:
        return render(request, 'usuarios/cadastro.html')


def fazer_login(request):
    if request.method == 'POST':
        #Coletando dados novamente
        username = request.POST.get('user').lower()
        senha = request.POST.get('password')
        
        #Utilizando o authenticate para verificar as informações coletadas
        user = authenticate(request, username=username, password=senha)

        #Se user, ou seja, se o usuário existir, e as credenciais estiverem corretas
        if user:
            
            #Realiza o login e redireciona
            login(request, user)
            return redirect('index')

        else:
            messages.error(request, 'Credenciais inválidas')
            return redirect('login')
        
    else:
        return render(request, 'usuarios/login.html')


def logout(request):

    #Realizando o logout, saída do usuário que realizou a requisição
    auth.logout(request) 
    return redirect('login')
