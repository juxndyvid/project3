from django.db import models

# Create your models here.
class Curso(models.Model):
    codigo = models.IntegerField(null=False)
    nombre = models.CharField(max_length=20)
    creditos = models.IntegerField(null=False)
