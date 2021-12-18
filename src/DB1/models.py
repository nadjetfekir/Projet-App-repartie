# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OperationcommercialeOperationcommerciale(models.Model):
    identifiant = models.AutoField(primary_key=True)
    type = models.CharField(max_length=14)
    # Field name made lowercase.
    margedegagee = models.FloatField(db_column='margeDegagee')
    # Field name made lowercase.
    nombrekm = models.FloatField(db_column='nombreKm')
    # Field name made lowercase.
    motcleresponsable = models.CharField(
        db_column='motCleResponsable', max_length=255)
    # Field name made lowercase.
    motcleclient = models.CharField(db_column='motCleClient', max_length=255)
    responsable = models.ForeignKey('PersonnelPersonnel', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'operationCommerciale_operationcommerciale'


class PersonnelPersonnel(models.Model):
    nom = models.TextField()
    prenom = models.TextField()
    etat = models.CharField(max_length=14)
    service = models.CharField(max_length=30)
    # Field name made lowercase.
    frequenceqardiaque = models.FloatField(db_column='frequenceQardiaque')
    # Field name made lowercase.
    tauxsudation = models.FloatField(db_column='tauxSudation')
    identifiant = models.AutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'personnel_personnel'
