from django.contrib.auth.models import User
from django import forms

#Criamos um arquivo forms.py, importamos nossa model, nesse caso uso a do django, User.
class CadastroForm(forms.ModelForm): #Criamos ua classe model form, herdando de forms.ModelForm
    password = forms.CharField(
        label = '',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Digite sua senha'
        })
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirme sua senha',
        })
    )

    class Meta: #Classe importante, vai falar o que será tratado dentro da classe
        model = User #Recebe a model
        fields = ['username', 'email'] #Campos que serão preenchidos. Se for todos, podemos: '__all__'

        widgets={
            'username': forms.TextInput(attrs={
                'placeholder': 'Digite um nome de usuário',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Insira seu e-mail',
            }),
        }

        labels={
            'username': '',
            'email': '',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
            
        self.fields['username'].help_text = ''