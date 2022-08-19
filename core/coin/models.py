from django.db import models
from datetime import datetime
# Create your models here.
class Cotacoes(models.Model):
    coin = models.CharField(max_length=200)
    valor = models.FloatField()
    dateCoin = models.DateTimeField(default=datetime.now, blank=True)
