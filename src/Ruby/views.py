from django.shortcuts import render
from django.db.models import Sum, Count
# from django.views.decorators import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from personnel.models import Personnel
from operationCommerciale.models import OperationCommerciale
import db_chili.models
import db_danemark.models
from api_direction_generale.serializers import PersonnelSerializer, OperationCommercialeSerializer
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView, TemplateView
# @csrf_exempt
from django.http import HttpResponse
import requests



def stat_france(request):

    number_employee_france = Personnel.objects.count()

    number_employee_chili = db_chili.models.Personnel.objects.using(
            'site_chili').count()

    number_employee_danemark = db_danemark.models.Personnel.objects.using(
            'site_danemark').count()

            
    nb_employee_total = number_employee_france + number_employee_chili + number_employee_danemark


    montant_total_france = OperationCommerciale.objects.filter(type="achat").aggregate(
            montant_total=Sum('margeDegagee'))['montant_total']
    montant_total_chili = db_chili.models.Operationcommerciale.objects.using("site_chili").filter(
            type="Achat").aggregate(montant_total=Sum('margedegagee'))['montant_total']
    montant_total_danemark = db_danemark.models.Operationcommerciale.objects.using("site_danemark").filter(
            type=1).aggregate(montant_total=Sum('marge_degage'))['montant_total']

    montant_total = montant_total_france + montant_total_chili + montant_total_danemark

    context={
        'montant':int(montant_total),
        'nb':nb_employee_total
    }
    return render(request, 'direction_generale.html', context=context)

def get_juridique(request):
    response = requests.get(
        'http://192.168.171.86:3000/machines/NombreEnPanneTousSites')
    panne=response.text
    response1 =  requests.get(
        'http://192.168.171.86:3000/personnels/maxJuridiqueTousSites')
    nb_max=response1.text
    context={
        'panne':panne,
        'nb_max':nb_max,
    }
    return render(request, 'service_juridique.html', context=context)

def get_cybersecurite(request):
    response = requests.get(
        'http://192.168.43.232:5000/surveillance/nombre_drone_panne')
    drone_panne=response.text
    response1 =  requests.get(
        'http://192.168.43.232:5000/formation/max_pourcentage_satisfaction')
    max_pourcentage_satisfaction=response1.text
    context={
        'drone':drone_panne,
        'max':max_pourcentage_satisfaction,
    }
    return render(request, 'service_cybersecurite.html', context=context)