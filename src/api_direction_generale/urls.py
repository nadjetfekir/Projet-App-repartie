from django.urls import path
from api_direction_generale import views

urlpatterns = [
    path('employee', views.get_employee),
    path('employee/number', views.get_employee_count),
    path('operationCommercial/', views.get_opertaionCommercial),
    path('operationCommercial/montant', views.get_montant),

]
