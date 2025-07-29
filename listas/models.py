from django.db import models
from django.contrib.auth.models import User

#Relação One-to-many. UM usuário pode ter VÁRIAS listas de compras. UMA lista pode ter VÁRIOS produtos
class ListaCompras(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listas') 

    nome = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

class Item(models.Model):
    lista = models.ForeignKey(ListaCompras, on_delete=models.CASCADE, related_name='itens')

    nome = models.CharField(max_length=100)
    quantidade = models.PositiveIntegerField(default=1)

