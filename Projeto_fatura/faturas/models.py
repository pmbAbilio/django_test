from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Fatura(models.Model):
    id = models.AutoField(primary_key=True)
    Vendedor = models.TextField(default="EDP")
    Data = models.DateField(default=timezone.now())
    imagemUrl = models.ImageField(
        default='default.jpg', upload_to='imagens_faturas')
    Descricao = models.TextField(default="Descrição da fatura", max_length=200)
    Valor = models.TextField(default="0,0€")
    Client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Fatura de {} do vendedor {}'.format(self.Data, self.Vendedor)

    def get_absolute_url(self):
        return reverse("Fatura", kwargs={"pk": self.pk})
