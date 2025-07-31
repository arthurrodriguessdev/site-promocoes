from django.shortcuts import render, redirect
from django.contrib.auth.models import User #Modelo de usuário do django
from django.contrib.auth import authenticate, login
from django.contrib import messages #Módulo de mensagens
from django.contrib import auth 
from usuarios.forms import CadastroForm

def cadastro(request):
    if request.method == 'GET':
        form = CadastroForm()
        formulario = {
            'form': form
        }

        return render(request, 'usuarios/cadastro.html', formulario)
    else:
        form = CadastroForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']

            if password != password2:
                messages.error(request, 'As senhas devem ser iguais')
                return redirect('cadastro')
            
            if len(password) < 8:
                messages.error(request, 'A senha deve ter, no mínimo, 8 caracteres')
                return redirect('cadastro')
            
            if User.objects.filter(email=email).exists():
                messages.error(request, 'E-mail já existente')
                return redirect('login')
            
            if User.objects.filter(username=username).exists():
                messages.error(request, 'O usuário já existe')
                return redirect('login')
            
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            print(user.password)

            return redirect('login')
        else:
            messages.error(request, 'Formulário inválido')
            return redirect('cadastro')


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
