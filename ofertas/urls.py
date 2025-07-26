from django.urls import path
from ofertas.views import index

urlpatterns = [
    path('', index, name='index')
]