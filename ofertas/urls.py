from django.urls import path
from ofertas.views import detalhamento_oferta, sobre_software, ListarOfertas

urlpatterns = [
    path('detalhamento/<int:id>', detalhamento_oferta, name='detalhamento'),
    path('index/listar', ListarOfertas.as_view(), name='listar_ofertas'),
    path('index/sobre', sobre_software, name='sobre_software'),
]