# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Operationcommerciale(models.Model):
    type = models.IntegerField()
    marge_degage = models.FloatField(blank=True, null=True)
    nb_kilo_parc = models.FloatField(blank=True, null=True)
    mot_cle_utilises_respo = models.CharField(
        max_length=100, blank=True, null=True)
    mot_cle_utilises_client = models.CharField(
        max_length=100, blank=True, null=True)
    responsable = models.ForeignKey(
        'Personnel', models.DO_NOTHING, db_column='responsable', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operationcommerciale'


class Personnel(models.Model):
    nom_prenom = models.CharField(max_length=100)
    etat = models.CharField(max_length=13)
    service = models.CharField(max_length=26)
    freq_card_actu = models.FloatField(blank=True, null=True)
    taux_sudation = models.FloatField(blank=True, null=True)
    position = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personnel'
