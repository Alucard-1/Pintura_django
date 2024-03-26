from django.db import models


class lista_clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    foto = models.ImageField(upload_to="fotos_clientes", blank=True, null=True)
