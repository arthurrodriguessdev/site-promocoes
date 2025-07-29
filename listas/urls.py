from django.urls import path, include
from listas.views import criar_lista

urlpatterns = [
    path('cria/lista', criar_lista, name='criar_lista')
]