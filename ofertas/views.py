from django.shortcuts import render, get_object_or_404
from ofertas.models import Oferta
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

@login_required(login_url='login')
def detalhamento_oferta(request, id):
    oferta = get_object_or_404(Oferta, id=id) #Pega o objeto que tem o ID específico ou erro 404 

    detalhamento = {
        'detalhes': oferta
    }

    return render(request, 'ofertas/detalhes_oferta.html', detalhamento)


class ListarOfertas(ListView):
    model = Oferta
    template_name = 'ofertas/index.html'
    context_object_name = 'ofertas'

    def get_queryset(self):
        ofertas = super().get_queryset().order_by('supermercado__nome_supermercado')
        search = self.request.GET.get('search')

        if search:
            ofertas = Oferta.objects.filter(supermercado__nome_supermercado__icontains=search).order_by('supermercado__nome_supermercado')
            
        return ofertas


def sobre_software(request):
    return render(request, 'ofertas/sobre.html')
