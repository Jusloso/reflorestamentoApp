from django.db import models
from PIL import Image

# Create your models here.
class Floresta(models.Model):
    ano = models.CharField(max_length=100)
    cultura = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    area = models.IntegerField()

    def __str__(self):
        return self.estado
