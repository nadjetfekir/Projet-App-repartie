from django.shortcuts import render
from django.db.models import Sum, Count
# from django.views.decorators import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from personnel.models import Personnel
from operationCommerciale.models import OperationCommerciale
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView, TemplateView
# @csrf_exempt
from django.http import HttpResponse

# Create your views here.


def get_montant_total(request):
    montant = OperationCommerciale.objects.aggregate(
        montant_total=Sum('margeDegagee'))
    html = "<html><body><h2>Le montant totale:</h2> est %d.</body></html>" % int(
        montant["montant_total"])
    return HttpResponse(html)


# http://192.168.117.86:3000/personnels/liste
