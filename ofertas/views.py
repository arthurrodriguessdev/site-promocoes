from django.shortcuts import render
from ofertas.models import Oferta

def index(request):
    oferta = Oferta.objects.all()
    ofertas = {
        'ofertas': oferta
    }

    return render(request, 'ofertas/index.html', ofertas)

def detalhamento_oferta(request):
    return render(request, 'ofertas/detalhes_oferta.html')
