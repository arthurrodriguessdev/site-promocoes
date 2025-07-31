from django import forms
from listas.models import ListaCompras

class ListaComprasForm(forms.ModelForm):
    class Meta:
        model = ListaCompras
        fields = ['nome']