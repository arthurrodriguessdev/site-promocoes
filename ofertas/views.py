from django.shortcuts import render

def index(request):
    ofertas = {
        'ofertas': [
            {'supermercado': 'Barbosa', 'descricao': 'arroz, feijao, macarrao'},
            {'supermercado': 'Esperança', 'descricao': 'carne, travesseiro, chcocolate'},
            {'supermercado': 'Brasil', 'descricao': 'sorvete, açaí, banana'},
            {'supermercado': 'Central', 'descricao': 'Arroz, Feijão, Açúcar'},
            {'supermercado': 'Nova Vida', 'descricao': 'Leite, Pão, Café'},
            {'supermercado': 'Bom Preço', 'descricao': 'Sabão em pó, Detergente, Amaciante'},
        ]
    }

    return render(request, 'ofertas/index.html', ofertas)
