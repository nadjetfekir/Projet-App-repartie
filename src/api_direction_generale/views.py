from django.shortcuts import render
from django.db.models import Sum, Count
# from django.views.decorators import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from personnel.models import Personnel
from operationCommerciale.models import OperationCommerciale
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
        filters = {}

        if etatQuery:
            filters['etat'] = etatQuery
        if serviceQuery:
            filters['service'] = serviceQuery

        number_employee = Personnel.objects.filter(**filters).count()
        return Response(number_employee)
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


def get_nb_panne(request):
    response = requests.get(
        'http://172.20.10.4:3000/machines/nombreEnPanne')
    print('//////////////////////')

    print(response.text)
    html = "<html><body><h2>Le nombre totale de machine en panne:</h2> est %s.</body></html>" % response.text
    return HttpResponse(html)


@api_view(['GET'])
def get_montant(request):
    if request.method == 'GET':
        typeQuery = request.query_params.get('type')
        responsableQuery = request.query_params.get('responsable')
        filters = {}

        if typeQuery:
            filters['type'] = typeQuery
        if responsableQuery:
            filters['responsable'] = responsableQuery

        montant_total = OperationCommerciale.objects.filter(
            **filters).aggregate(montant_total=Sum('margeDegagee'))
        return Response(montant_total)
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

        print(operations_vente)
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


def get_montantA(request):
    montant = OperationCommerciale.objects.aggregate(
        montant_total=Sum('margeDegagee'))
    html = "<html><body><h2>Le montant totale:</h2> est %d.</body></html>" % int(
        montant["montant_total"])
    return HttpResponse(html)


"""
def get_montantA(request):
    context = {}
    context['montant'] = OperationCommerciale.objects.aggregate(
        montant_total=Sum('margeDegagee'))
    return render(request, 'api_direction_generale/montant.html', context)
"""
