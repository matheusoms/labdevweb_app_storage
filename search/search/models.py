from django.db import models


class UsuarioModel(models.Model):
    cpf = models.CharField('cpf', max_length=11, unique=True,default='temp_cpf')
    nome = models.CharField('nome', max_length=30)
    telefone = models.CharField('telefone', max_length=11)
    email = models.CharField('email', max_length=30,default='temp@example.com')
    user_type = models.CharField('user_type', max_length=10, default='usuario')
    password = models.CharField('senha', max_length=15,default='temporary_hash')
  

class LoginModel(models.Model):
    cpf = models.CharField('cpf', max_length=11,default='temp_cpf')
    password = models.CharField('password', max_length=15, default='temporary_hash')

