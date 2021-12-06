from django.db import models

# Create your models here.
from django.db import models

from personnel.models import Personnel


class OperationCommerciale(models.Model):
    identifiant = models.IntegerField(default=0, primary_key=True)

    class Type(models.TextChoices):
        ACHAT = 'achat'
        VENTE = 'vente'

    type = models.CharField(
        max_length=14, choices=Type.choices,)

    responsable = models.ForeignKey(
        Personnel, on_delete=models.CASCADE, null=False,)

    margeDegagee = models.FloatField()

    nombreKm = models.FloatField()

    motCleResponsable = models.CharField(max_length=255,)

    motCleClient = models.CharField(max_length=255,)
