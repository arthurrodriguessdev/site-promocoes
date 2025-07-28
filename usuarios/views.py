from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == "POST":
        print('usuario criado com sucesso')
    

    

    return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def logout(request):
    return render(request, 'usuarios/logout.html')
