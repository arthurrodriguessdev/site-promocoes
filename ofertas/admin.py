from django.contrib import admin
from ofertas.models import Oferta, Supermercado

#Registrando model no admin (django admin)
class OfertaAdmin(admin.ModelAdmin):
    list_display = ['supermercado', 'produtos_em_promocao', 'data_criacao', 'titulo_promocao', 'inicio_promocao', 'fim_promocao']
    search_fields = ['titulo_promocao']

class SupermercadoAdmin(admin.ModelAdmin):
    list_display = ['nome_supermercado', 'endereco_supermercado', 'numero_telefone']
    search_fields = ['nome_supermercado']
    
admin.site.register(Oferta)
admin.site.register(Supermercado)
