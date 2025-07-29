from django.shortcuts import render, redirect
from django.contrib import messages #Módulo de mensagens
from django.contrib.auth.models import User

def cadastro(request):
    if request.method == "POST": #Se o botão de criar conta for clicado, renderiza pag login
        #A variável vai receber o que o usuário preencher, se for get ou post
        user = request.POST.get('user') #O que está dentro do parêntese é o 'name' do template
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2') #Confirmação de senha

        if not user.strip():
            messages.error(request, 'Preencha o campo de usuário corretamente')
            return redirect('cadastro')
        
        if not email.strip():
            messages.error(request, 'Preencha o campo de e-mail corretamente')
            return redirect('cadastro')

        if senha != senha2:
            messages.error(request, 'As senhas devem ser iguais')
            return redirect('cadastro')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Usuário já cadastrado')
            return redirect('login')
        
        user = User.objects.create_user(username=user, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário criado com sucesso')

        return redirect('login')
    
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def logout(request):
    return render(request, 'usuarios/logout.html')
