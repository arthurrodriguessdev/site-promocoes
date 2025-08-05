from django.db import models
from datetime import date

#Criando as models dos cards ofertas
class Supermercado(models.Model):
    nome_supermercado = models.CharField("Nome do supermercado", max_length=100)
    endereco_supermercado = models.TextField("Endereço do estabelecimento", blank=False, default="Endereço não informado")
    numero_telefone = models.CharField("Telefone do estabelecimento", default="Não informado", max_length=15)

    def __str__(self):
        return self.nome_supermercado
    
class Oferta(models.Model):
    supermercado = models.ForeignKey(Supermercado, on_delete=models.PROTECT, related_name='oferta_supermercado')
    produtos_em_promocao = models.TextField("Produtos em Promoção")
    data_criacao = models.DateTimeField(auto_now=True)
    titulo_promocao = models.CharField("Título da Promoção", max_length=100, default="Oferta especial")
    inicio_promocao = models.DateField("Data de início", default=date.today)
    fim_promocao = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo_promocao
