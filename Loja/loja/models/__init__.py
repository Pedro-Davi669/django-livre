from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
#acima são bibliotecas padrões necessárias do Django, e abaixo nossos models
from .Fabricante import Fabricante
from .Categoria import Categoria
from .Produtos import Produto
PERFIL = (
    (1, 'admin'),
    (2, 'usuario')
)
from .Usuario import  Usuario
