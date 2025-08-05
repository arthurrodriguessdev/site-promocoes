from django.urls import path
from ofertas.views import index, detalhamento_oferta, sobre_software, listar_ofertas

urlpatterns = [
    path('index/', index, name='index'),
    path('detalhamento/<int:id>', detalhamento_oferta, name='detalhamento'),
    path('index/listar', listar_ofertas, name='listar_ofertas'),
    path('index/sobre', sobre_software, name='sobre_software'),
]