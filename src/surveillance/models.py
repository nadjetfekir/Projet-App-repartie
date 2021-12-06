from django.db import models
from multiselectfield import MultiSelectField
from zone.models import Zone
# Create your models here.
from django.db import models
class SurveillanceZone(models.Model):
    zone = models.ForeignKey(
        Zone, on_delete=models.CASCADE, null=False,)
    nbDronesActives = models.IntegerField( default=0)
    nbDronesEnPanne = models.IntegerField( default=0)
    nbDronesEnRechargement = models.IntegerField( default=0)
    detectionIncendie=  models.BooleanField(default=False)
    auditConformite=  models.BooleanField(default=False)

    class DetectionForme(models.TextChoices):
        Aucune = 'aucune'
        PersonnelNonIdentifiee = 'personnel non identifiée'
        ObjetNonIdentifiee = 'objet non identifiee'
    
    detectionForme = models.CharField(max_length=50, choices=DetectionForme.choices, default=DetectionForme.Aucune, )

    
