from django.urls import path
from ofertas.views import index, detalhamento_oferta

urlpatterns = [
    path('', index, name='index'),
    path('detalhamento', detalhamento_oferta, name='detalhamento')
]