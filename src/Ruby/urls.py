from django.urls import path, re_path
from Ruby import views

urlpatterns = [
    path('direction_generale', views.stat_france,name='service_dir'),
    path('service_jur', views.get_juridique,name='service_jur'),
    path('service_cyber', views.get_cybersecurite,name='cybersecurite'),
]