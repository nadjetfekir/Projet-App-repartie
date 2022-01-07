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
        responsableQuery = request.query_params.get('responsable')
        siteQuery = request.query_params.get('site')
        filters = {}

        if typeQuery:
            filters['type'] = typeQuery
        if responsableQuery:
            filters['responsable'] = responsableQuery

        montant_total_france = OperationCommerciale.objects.filter(
            **filters).aggregate(montant_total=Sum('margeDegagee'))['montant_total']

        montant_total_chili = db_chili.models.Operationcommerciale.objects.using("site_chili").filter(
            **filters).aggregate(montant_total=Sum('margedegagee'))['montant_total']

        montant_total_danemark = db_danemark.models.Operationcommerciale.objects.using("site_danemark").filter(
            **filters).aggregate(montant_total=Sum('marge_degage'))['montant_total']

        if siteQuery == None:
            montant_total = {'montant_total': montant_total_france +
                             montant_total_chili + montant_total_danemark}
            return Response(montant_total)
        else:
            if siteQuery == "France":
                return Response(montant_total_france)
            elif siteQuery == "Chili":
                return Response(montant_total_chili)
            elif siteQuery == "Danemark":
                return Response(montant_total_danemark)
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



def get_montantA(request):
    montant = OperationCommerciale.objects.aggregate(
        montant_total=Sum('margeDegagee'))
    html = "<html><body><h2>Le montant totale:</h2> est %d.</body></html>" % int(
        montant["montant_total"])
    return HttpResponse(html)


def get_nb_panne(request):
    response = requests.get(
        'http://172.20.10.4:3000/machines/nombreEnPanne')
    print('//////////////////////')

    print(response.text)
    html = "<html><body><h2>Le nombre totale de machine en panne:</h2> est %s.</body></html>" % response.text
    return HttpResponse(html)


"""
def get_montantA(request):
    context = {}
    context['montant'] = OperationCommerciale.objects.aggregate(
        montant_total=Sum('margeDegagee'))
    return render(request, 'api_direction_generale/montant.html', context)
"""

def get_montant_total(request):
    montant = OperationCommerciale.objects.aggregate(montant_total=Sum('margeDegagee'))
    context={
        'montant':int(montant["montant_total"]),
    }
    return render(request, 'montant.html', context=context)

def stat_france(request):
    nb=Personnel.objects.count()+db_chili.models.Personnel.objects.using(
            'site_chili').count()+db_danemark.models.Personnel.objects.using(
            'site_danemark').count()
    montant = OperationCommerciale.objects.aggregate(montant_total=Sum('margeDegagee'))
    context={
        'montant':int(montant["montant_total"]),
        'nb':nb
    }
    return render(request, 'montant.html', context=context)

def get_juridique(request):
    montant = OperationCommerciale.objects.aggregate(montant_total=Sum('margeDegagee'))
    context={
        'montant':int(montant["montant_total"]),
    }
    return render(request, 'service_juridique.html', context=context)