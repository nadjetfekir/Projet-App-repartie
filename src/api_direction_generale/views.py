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


@api_view(['GET'])
def get_employee_count(request):
    if request.method == 'GET':
        etatQuery = request.query_params.get('etat')
        serviceQuery = request.query_params.get('service')
        siteQuery = request.query_params.get('site')
        filters = {}

        if etatQuery:
            filters['etat'] = etatQuery
        if serviceQuery:
            filters['service'] = serviceQuery

        number_employee_france = Personnel.objects.filter(**filters).count()

        number_employee_chili = db_chili.models.Personnel.objects.using(
            'site_chili').filter(**filters).count()

        number_employee_danemark = db_danemark.models.Personnel.objects.using(
            'site_danemark').filter(**filters).count()

        if siteQuery == None:
            return Response(number_employee_france + number_employee_chili + number_employee_danemark)
        else:
            if siteQuery == "France":
                return Response(number_employee_france)
            elif siteQuery == "Chili":
                return Response(number_employee_chili)
            elif siteQuery == "Danemark":
                return Response(number_employee_danemark)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_employee(request):
    if request.method == 'GET':
        etatQuery = request.query_params.get('etat')
        serviceQuery = request.query_params.get('service')
        filters = {}

        if etatQuery:
            filters['etat'] = etatQuery
        if serviceQuery:
            filters['service'] = serviceQuery

        employees = Personnel.objects.filter(**filters).all()
        serializer = PersonnelSerializer(employees, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_montant(request):
    if request.method == 'GET':
        typeQuery = request.query_params.get('type')
        #responsableQuery = request.query_params.get('responsable')
        siteQuery = request.query_params.get('site')
        filters_france = {}
        filters_chili = {}
        filters_danemark = {}

        if typeQuery:
            filters_france['type'] = typeQuery
            if typeQuery == "achat":
                filters_chili["type"] = "Achat"
                filters_danemark["type"] = 1
            else:
                filters_chili["type"] = "Vente"
                filters_danemark["type"] = 0

        montant_total_france = OperationCommerciale.objects.filter(**filters_france).aggregate(
            montant_total=Sum('margeDegagee'))['montant_total']

        montant_total_chili = db_chili.models.Operationcommerciale.objects.using("site_chili").filter(
            **filters_chili).aggregate(montant_total=Sum('margedegagee'))['montant_total']

        montant_total_danemark = db_danemark.models.Operationcommerciale.objects.using("site_danemark").filter(
            **filters_danemark).aggregate(montant_total=Sum('marge_degage'))['montant_total']

        if siteQuery == None:
            montant_total = {'montant_total': montant_total_france +
                             montant_total_chili + montant_total_danemark}
            return Response(montant_total)
        else:
            if siteQuery == "France":
                return Response({'montant_total': montant_total_france})
            elif siteQuery == "Chili":
                return Response({'montant_total': montant_total_chili})
            elif siteQuery == "Danemark":
                return Response({'montant_total': montant_total_danemark})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_opertaionCommercial(request):
    if request.method == 'GET':
        typeQuery = request.query_params.get('type')
        responsableQuery = request.query_params.get('responsable')
        filters = {}

        if typeQuery:
            filters['type'] = typeQuery
        if responsableQuery:
            filters['responsable'] = responsableQuery

        operationCommercials = OperationCommerciale.objects.filter(
            **filters).all()
        serializer = OperationCommercialeSerializer(
            operationCommercials, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_best_employee(request):
    # top 3 employee
    if request.method == 'GET':

        operations_vente = OperationCommerciale.objects.filter(type='vente').values('responsable').annotate(
            montant_total=Sum('margeDegagee'), nombre_operation=Count('identifiant')).order_by('-montant_total')[:3]

        # print(operations_vente)
        results = []
        for item in operations_vente:
            personnel = Personnel.objects.get(pk=item['responsable'])
            serializer = PersonnelSerializer(personnel)
            results.append({'personnel': serializer.data,
                            'marge de vente total': item['montant_total'],
                            "nombre d'opperations de vente réalisées": item['nombre_operation']})

        return Response(results)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


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