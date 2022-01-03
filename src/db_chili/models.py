# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Operationcommerciales(models.Model):
    id = models.IntegerField(primary_key=True)
    # Field name made lowercase.
    identifiant = models.IntegerField(
        db_column='Identifiant', blank=True, null=True)
    # Field name made lowercase.
    type = models.CharField(
        db_column='Type', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    margedegagee = models.FloatField(
        db_column='MargeDegagee', blank=True, null=True)
    # Field name made lowercase.
    nombrekmparcourus = models.FloatField(
        db_column='NombreKmParcourus', blank=True, null=True)
    # Field name made lowercase.
    motresponsable = models.CharField(
        db_column='MotResponsable', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    motclientfournisseur = models.CharField(
        db_column='MotClientFournisseur', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')
    # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')
    # Field name made lowercase.
    responsable = models.CharField(
        db_column='Responsable', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'OperationCommerciales'


class Personnels(models.Model):
    id = models.IntegerField(primary_key=True)
    # Field name made lowercase.
    nomprenom = models.CharField(
        db_column='NomPrenom', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    etat = models.CharField(
        db_column='Etat', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    service = models.CharField(
        db_column='Service', max_length=255, blank=True, null=True)
    # Field name made lowercase.
    frequencecardiaque = models.FloatField(
        db_column='FrequenceCardiaque', blank=True, null=True)
    # Field name made lowercase.
    tauxsaudation = models.FloatField(
        db_column='TauxSaudation', blank=True, null=True)
    # Field name made lowercase.
    positionlatitude = models.FloatField(
        db_column='PositionLatitude', blank=True, null=True)
    # Field name made lowercase.
    positionlongitude = models.FloatField(
        db_column='PositionLongitude', blank=True, null=True)
    # Field name made lowercase.
    createdat = models.DateTimeField(db_column='createdAt')
    # Field name made lowercase.
    updatedat = models.DateTimeField(db_column='updatedAt')
    # Field name made lowercase.
    identifiant = models.CharField(
        db_column='Identifiant', max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Personnels'
