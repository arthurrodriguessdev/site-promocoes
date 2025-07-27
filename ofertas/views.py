from django.shortcuts import render, get_object_or_404
from ofertas.models import Oferta

def index(request):
    oferta = Oferta.objects.all()
    ofertas = {
        'ofertas': oferta
    }

    return render(request, 'ofertas/index.html', ofertas)

def detalhamento_oferta(request, id):
    oferta = get_object_or_404(Oferta, id=id)

    detalhamento = {
        'detalhes': oferta
    }

    return render(request, 'ofertas/detalhes_oferta.html', detalhamento)
