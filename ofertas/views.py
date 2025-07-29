from django.shortcuts import render, get_object_or_404
from ofertas.models import Oferta
from django.contrib.auth.decorators import login_required

def index(request):
    oferta = Oferta.objects.all() #Pega todos os objetos do banco de dados e salva na variável
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
