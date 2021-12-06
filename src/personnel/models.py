from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
from django.db import models
class Personnel(models.Model):
    identifiant = models.IntegerField( default=0,primary_key=True)
    nom=models.TextField()
    prenom=models.TextField()
    class Etat(models.TextChoices):
        ACTIF = 'actif'
        REPOS = 'repos'
        ARRET = 'arret maladie'
        CONGE = 'congé'
    
    etat = models.CharField(max_length=14, choices=Etat.choices, default=Etat.ACTIF, )

    class Service(models.TextChoices):
        COMMERCIAL = 'commercial'
        FINANCE = 'finance et gestion'
        RESSOURCE = 'ressources humaines'
        JURIDIQUE = 'juridique'
        LOGISTIQUE = 'logistique'
        ASSISTANCECom = 'assistance commerciale'
        DIRECTION = 'direction générale'
        MAINTENANCE = 'maintenance'
        ACHATS = 'achats'
        CYBER = 'cyber sécurité'
        RECHERCHE = 'recherche et développement'
        INFORMATIQUE = 'informatique'
        QUALITE = 'qualité'
        COLLECTE = 'collecte'
        MARKETING = 'marketing'
        INDUSTRIEL = 'industriel'
        ASSISTANCETech = 'assistance technique'
        ANALYSE = 'analyse des données'

    service = models.CharField(max_length=30, choices=Service.choices,  )
    frequenceQardiaque = models.FloatField()
    tauxSudation = models.FloatField()

    