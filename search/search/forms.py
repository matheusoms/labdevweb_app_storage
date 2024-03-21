from django import forms   
from .models import UsuarioModel, LoginModel

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuarioModel
        fields = ['nome','cpf','telefone','email','password']

class LoginForm(forms.ModelForm):
    class meta:
        model = LoginModel
        fields=['cpf','password']