from django.db.models import fields
from rest_framework import serializers
from django.db import models
from personnel.models import Personnel
from operationCommerciale.models import OperationCommerciale

#from DB1.models import PersonnelPersonnel, OperationcommercialeOperationcommerciale


class PersonnelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personnel
        fields = ['identifiant', 'etat', 'service']


class OperationCommercialeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationCommerciale
        fields = ['identifiant', 'type', 'responsable', 'margeDegagee']
