from django.urls import path
from usuarios.views import cadastro, fazer_login, logout

urlpatterns = [
    path('cadastro', cadastro, name='cadastro'),
    path('', fazer_login, name='login'),
    path('logout', logout, name='logout'),
]