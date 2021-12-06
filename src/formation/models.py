from django.db import models
from personnel.models import Personnel
from multiselectfield import MultiSelectField

# Create your models here.
from django.db import models
class Formation(models.Model):
    nomFormation = models.CharField(max_length=255, blank=True)
    sujet = models.TextField()
    date = models.DateTimeField()
    pourcentageEngagement = models.FloatField()
    pourcentageSatisfaction = models.FloatField()
    MotCleFormateur = models.CharField(max_length=255)
    MotClePersonnel = models.CharField(max_length=255)
    personnels=models.ManyToManyField(Personnel)



    