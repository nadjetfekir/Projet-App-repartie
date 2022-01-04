from django.urls import path, re_path
from api_direction_generale import views

urlpatterns = [
    path('employee', views.get_employee),
    path('employee/number', views.get_employee_count),
    path('employee/best_employee', views.get_best_employee),
    path('operationCommercial/', views.get_opertaionCommercial),
    path('operationCommercial/montant', views.get_montant),
    #path('montants', views.get_montant),
    #path('panne', views.get_nb_panne),


]
