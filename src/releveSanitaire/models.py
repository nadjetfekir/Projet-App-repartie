from django.db import models

# Create your models here.
from django.db import models

from zone.models import Zone


class ReleveSanitaire(models.Model):

    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, null=False,)

    identifiant = models.IntegerField(default=0, unique=True)

    temprature = models.FloatField()

    humidite = models.FloatField()  # %

    pressionAir = models.FloatField()

    oxydeCarbone = models.FloatField()

    particule = models.FloatField()  # (PM10 et PM2.5)
