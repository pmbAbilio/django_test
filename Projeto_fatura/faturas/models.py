from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Fatura(models.Model):
    id = models.AutoField(primary_key=True)
    Vendedor = models.TextField(default="EDP")
    Data = models.DateField(default=timezone.now())
    imagemUrl = models.TextField(default="pasta/nomeImagem.jpeg")
    Descricao = models.TextField(default="Descrição da fatura")
    Valor = models.TextField(default="0,0€")
    Client = models.ForeignKey(User, on_delete=models.CASCADE)
