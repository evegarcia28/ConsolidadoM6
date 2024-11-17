from django.urls import path
from . import views

app_name='vehiculo'

urlpatterns= [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.agregar_vehiculo, name='agregar_vehiculo'),
    path('vehiculo/list/', views.listar_vehiculos, name='listar_vehiculos'),
    
]