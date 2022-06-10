from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils import timezone
from django.utils.timezone import now
from django.urls import reverse
from django import template
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime


# Create your models here.
class TipoDespesa(models.Model):
    nome = models.CharField(max_length=100,blank=False, null=True)
    descricao = models.CharField(max_length=300,blank=False, null=True)
    valor_normal = models.DecimalField(max_digits=7, decimal_places=3, blank=False, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    user = models.IntegerField(blank=True, null=False) # Blank Significa que nao precisamos de introduzir valor manualmente!

    def __str__(self):
        return self.nome

    def get_detalhes_url(self):
        return reverse("tipodespesa-detalhes-view", kwargs={"my_id": self.id})

    def get_elimina_url(self):
        return reverse("tipodespesa-elimina-view", kwargs={"my_id": self.id})


class Despesa(models.Model):
    nome = models.CharField(max_length=100,blank=True, null=True)
    descricao = models.CharField(max_length=300,blank=True, null=True)
    valor = models.DecimalField(max_digits=7, decimal_places=2, blank=False, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True, blank=False, null=True)
    user = models.IntegerField(blank=True, null=False)
    tipo_despesa = models.ForeignKey(TipoDespesa, on_delete=models.SET_NULL, null=True)
    # on_delte=models.SET_NULL permite que possamos eliminar um tipo de despesa, sem as despesas serem eliminadas tmb em cascada, mas mesmo assim nao podemos deixar eliminar um tipo de despesa se tiver despesas associadas!

    def __str__(self):
        return self.nome


class Receita(models.Model):
    nome = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=300, blank=True, null=True)
    valor = models.FloatField(validators=[MaxValueValidator(1000000), MinValueValidator(0)], blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    user = models.IntegerField(blank=False, null=False)

    def __str__(self):
        return self.nome