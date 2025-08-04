from django.shortcuts import render, redirect, get_object_or_404
from listas.models import ListaCompras, Item
from django.contrib.auth.models import User
from django.contrib import messages
from listas.forms import ListaComprasForm

def criar_lista(request):
    if request.method == 'POST':
        form = ListaComprasForm(request.POST)

        if form.is_valid():
            nome = form.cleaned_data['nome']

            if ListaCompras.objects.filter(nome=nome, usuario=request.user).exists():
                messages.error(request, 'Você já possui uma lista com esse nome')
                return redirect('criar_lista')
            
            lista = ListaCompras.objects.create(nome=nome, usuario=request.user)

            item_1 = request.POST.get('item_1')
            item_2 = request.POST.get('item_2')
            qtd_1 = request.POST.get('qtd_1')
            qtd_2 = request.POST.get('qtd_2')

            if item_1 and item_2:
                Item.objects.create(lista=lista, nome_item=item_1, quantidade=qtd_1)
                Item.objects.create(lista=lista, nome_item=item_2, quantidade=qtd_2)

                messages.success(request, 'Lista de compras criada com sucesso')
                return redirect('minha_lista')

        return redirect('minha_lista')

    else:
        form = ListaComprasForm()
        formulario = {
            'form': form
        }

        return render(request, 'listas/criar_lista.html', formulario)


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

def editar_lista(request, id_lista):
    lista = get_object_or_404(ListaCompras, id=id_lista, usuario=request.user)
    lista_itens = {
        'lista': lista
    }

    if request.method == 'POST':
        item_1v = request.POST.get('item_1')
        item_2v = request.POST.get('item_2')
        qtd_1v = request.POST.get('qtd_1')
        qtd_2v = request.POST.get('qtd_2')

        itens = Item.objects.filter(lista=lista)
        
        if len(itens) >= 2:
            itens[0].nome_item = item_1v
            itens[0].quantidade = qtd_1v
            itens[0].save()

            itens[1].nome_item = item_2v
            itens[1].quantidade = qtd_2v
            itens[1].save()

            messages.success(request, 'Lista atualizada com sucesso')
            return redirect('minha_lista')

        return redirect('minha_lista')
    
    else:
        return render(request, 'listas/editar_lista.html', lista_itens)
    

def excluir_lista(request, ide):
    lista = get_object_or_404(ListaCompras, id=ide, usuario=request.user)
    lista.delete()

    return redirect('minha_lista')
