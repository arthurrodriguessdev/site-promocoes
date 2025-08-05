from django.shortcuts import render, get_object_or_404
from ofertas.models import Oferta
from django.contrib.auth.decorators import login_required

def index(request):
    oferta = Oferta.objects.all().order_by('supermercado__nome_supermercado') #Pega todos os objetos do banco de dados e salva na variável
    ofertas = {
        'ofertas': oferta
    }

    return render(request, 'ofertas/index.html', ofertas)

@login_required(login_url='login')
def detalhamento_oferta(request, id):
    oferta = get_object_or_404(Oferta, id=id) #Pega o objeto que tem o ID específico ou erro 404 

    detalhamento = {
        'detalhes': oferta
    }

    return render(request, 'ofertas/detalhes_oferta.html', detalhamento)


def listar_ofertas(request):
    search = request.GET.get('search')

    if search:
        oferta = Oferta.objects.filter(supermercado__nome_supermercado__icontains=search).order_by('supermercado__nome_supermercado')
    else:
        oferta = Oferta.objects.all().order_by('nome_supermercado')

    ofertas = {
        'ofertas': oferta
    }

    return render(request, 'ofertas/index.html', ofertas)


def sobre_software(request):
    return render(request, 'ofertas/sobre.html')
