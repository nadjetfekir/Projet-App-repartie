from django.db import models

# Create your models here.
from django.db import models


class Zone(models.Model):
    identifiant = models.IntegerField(default=0, primary_key=True)
