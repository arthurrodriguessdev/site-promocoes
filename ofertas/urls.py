from django.urls import path
from ofertas.views import index, detalhamento_oferta

urlpatterns = [
    path('index/', index, name='index'),
    path('detalhamento/<int:id>', detalhamento_oferta, name='detalhamento')
]