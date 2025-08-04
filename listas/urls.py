from django.urls import path, include
from listas.views import criar_lista, minha_lista, exibir_lista, editar_lista, excluir_lista

urlpatterns = [
    path('cria/lista', criar_lista, name='criar_lista'),
    path('minha/lista/lista', minha_lista, name='minha_lista'),
    path('exibir/lista/<int:id>', exibir_lista, name='exibir_lista'),
    path('editar/lista/<int:id_lista>', editar_lista, name='editar_lista'),
    path('apagar/lista/<int:ide>', excluir_lista, name='excluir_lista')
]