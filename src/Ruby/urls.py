from django.urls import path, re_path
from Ruby import views

urlpatterns = [
    path('montant_total', views.get_montant_total),
]
