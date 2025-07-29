from django.shortcuts import render, redirect
from listas.models import ListaCompras, Item
from django.contrib.auth.models import User

def criar_lista(request):
    if request.method == 'POST':
        nome_lista = request.POST.get('nome_lista')
        item_1 = request.POST.get('item_1')
        item_2 = request.POST.get('item_2')
        qtd_1 = request.POST.get('qtd_1')
        qtd_2 = request.POST.get('qtd_2')

        lista = ListaCompras.objects.create(usuario=request.user, nome=nome_lista) #Lista recebe a instanciação do modelo

        if item_1 and item_2:
            Item.objects.create(lista=lista, quantidade=qtd_1)
            Item.objects.create(lista=lista, quantidade=qtd_2)

            print(nome_lista)
            print(item_1)
            print(item_2)
            print(qtd_1)
            print(qtd_2)
            print(lista.usuario)

            return redirect('login')

    return render(request, 'listas/criar_lista.html')
