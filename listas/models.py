from django.db import models
from django.contrib.auth.models import User

# Relação One-to-Many: Um usuário pode ter várias listas de compras
class ListaCompras(models.Model):
    # Chave estrangeira para o usuário dono da lista
    # on_delete=models.CASCADE: se o usuário for deletado, suas listas também serão deletadas
    # related_name='listas' permite acessar as listas do usuário via user.listas.all()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listas') 
    
    # Nome da lista de compras
    nome = models.CharField(max_length=100)
    
    # Data e hora em que a lista foi criada automaticamente
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Lista: {self.nome} ({self.usuario.username})'

# Relação One-to-Many: Uma lista pode ter vários itens
class Item(models.Model):
    # Chave estrangeira para a lista a que o item pertence
    # on_delete=models.CASCADE: se a lista for deletada, os itens dela também serão deletados
    # related_name='itens' permite acessar os itens da lista via lista.itens.all()
    lista = models.ForeignKey(ListaCompras, on_delete=models.CASCADE, related_name='itens')

    # Nome do item (produto)
    nome = models.CharField(max_length=100)
    
    # Quantidade do item (valor positivo)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Item: {self.nome} ({self.quantidade})'