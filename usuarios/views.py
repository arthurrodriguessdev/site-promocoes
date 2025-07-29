from django.shortcuts import render, redirect

def cadastro(request):
    if request.method == "POST": #Se o botão de criar conta for clicado, renderiza pag login
        return redirect('login')
    else:
        return render(request, 'usuarios/cadastro.html')


def login(request):
    return render(request, 'usuarios/login.html')


def logout(request):
    return render(request, 'usuarios/logout.html')
