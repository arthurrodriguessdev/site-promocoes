from django.shortcuts import render

def criar_lista(request):
    return render(request, 'listas/criar_lista.html')
