from collections import UserDict
from imaplib import _Authenticator
from django.shortcuts import render
from .models import UsuarioModel, LoginModel
from .forms import UsuarioForm, UsuarioModel,LoginModel
from validate_docbr import CPF, CNPJ
from django.contrib.auth import login as login_django
from . import views
from django.shortcuts import render, redirect
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm





def cadastro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        cpf_validator = CPF()
        if not cpf_validator.validate(form.data['cpf']):
            messages.error(request, 'CPF inválido!')
        elif UsuarioModel.objects.filter(cpf=form.data['cpf']).exists():
            messages.error(request, 'Usuario já foi cadastrado!')
        else:
            cliente = UsuarioModel()
            cliente.cpf = form.data['cpf']
            cliente.nome = form.data['nome']
            cliente.telefone = form.data['telefone']
            cliente.email = form.data['email']
            cliente.password = form.data['password']
            cliente.save()
            cliente = UserDict.objects.create_user(username = form.data['cpf'], password = form.data ['password'])
            cliente.save()
    return render(request, 'cadastro.html')





def login(request):
     if request.method == 'GET':
        return render(request, 'login.html') 
     else:
        username = request.POST.get('cpf')
        password = request.POST.get('password')

        user = _Authenticator(username = username , password = password)
        if user:
            login_django(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html')
    
     return render(request, 'login.html')  


