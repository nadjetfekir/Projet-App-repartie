from django.shortcuts import render
from django.db.models import Sum
# from django.views.decorators import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from personnel.models import Personnel
from operationCommerciale.models import OperationCommerciale
from api_direction_generale.serializers import PersonnelSerializer, OperationCommercialeSerializer


# @csrf_exempt


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
