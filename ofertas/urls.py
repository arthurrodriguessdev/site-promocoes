from django.urls import path
from ofertas.views import index, detalhamento_oferta, sobre_software

urlpatterns = [
    path('index/', index, name='index'),
    path('detalhamento/<int:id>', detalhamento_oferta, name='detalhamento'),
    path('index/sobre', sobre_software, name='sobre_software')
]