# Generated by Django 5.2.4 on 2025-07-26 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_supermercado', models.CharField(max_length=100, verbose_name='Nome do Supermercado')),
                ('produtos_em_promocao', models.TextField(verbose_name='Produtos em Promoção')),
                ('data_criacao', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
