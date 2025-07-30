from django.shortcuts import render, redirect, get_object_or_404
from listas.models import ListaCompras, Item
from django.contrib.auth.models import User
from django.contrib import messages

def criar_lista(request):
    if request.method == 'POST':
        
        #Pega os dados preenchidos no formulário
        nome_lista = request.POST.get('nome_lista')
        item_1 = request.POST.get('item_1')
        item_2 = request.POST.get('item_2')
        qtd_1 = request.POST.get('qtd_1')
        qtd_2 = request.POST.get('qtd_2')

        #Lista recebe o objeto, agora ela é um objeto. (preenche as lacunas de models)
        lista = ListaCompras.objects.create(usuario=request.user, nome=nome_lista) 

        if item_1 and item_2:
            Item.objects.create(lista=lista, nome=item_1, quantidade=qtd_1)
            Item.objects.create(lista=lista, nome=item_2, quantidade=qtd_2)

            messages.success(request, 'Lista criada com sucesso')
            return redirect('minha_lista')

    return render(request, 'listas/criar_lista.html')


def minha_lista(request):

    #lista recebe o filtro que é feito usando o usuário
    lista = ListaCompras.objects.filter(usuario=request.user)
    return render(request, 'listas/minha_lista.html', {'lista': lista})


def exibir_lista(request, id):
    lista = get_object_or_404(ListaCompras, id=id, usuario=request.user) #Tenta pegar o objeto dentro de ListaCompras ou erro 404
    itens = Item.objects.filter(lista=lista) #Filtra os itens, passando como parâmetro as listas

    contexto = {
        'lista': lista,
        'item': itens,
    }

    return render(request, 'listas/exibir_lista.html', contexto)