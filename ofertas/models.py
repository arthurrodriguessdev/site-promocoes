from django.db import models

#Criando as models dos cards ofertas
class Oferta(models.Model):
    nome_supermercado = models.CharField("Nome do Supermercado", max_length=100)
    produtos_em_promocao = models.TextField("Produtos em Promoção")
    data_criacao = models.DateTimeField(auto_now=True)
