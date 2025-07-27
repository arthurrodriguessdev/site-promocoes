from django.db import models
from datetime import date

#Criando as models dos cards ofertas
class Oferta(models.Model):
    nome_supermercado = models.CharField("Nome do Supermercado", max_length=100)
    produtos_em_promocao = models.TextField("Produtos em Promoção")
    data_criacao = models.DateTimeField(auto_now=True)
    titulo_promocao = models.CharField("Título da Promoção", max_length=100, default="Oferta especial")
    inicio_promocao = models.DateField("Data de início", default=date.today)
    fim_promocao = models.DateField(null=True, blank=True)
    endereco_supermercado = models.TextField("Endereço do estabelecimento", blank=False, default="Endereço não informado")
    numero_telefone = models.CharField("Telefone do estabelecimento", default="Não informado", max_length=15)
