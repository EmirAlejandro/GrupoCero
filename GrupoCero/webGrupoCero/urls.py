
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('', index,name='ind'),
    path('galeria/',galeria,name='gal'),
    path('login/',login_vista,name='LOGIN'),
    path('Registro/',Registro,name='reg'),
    path('quienes/',quienes,name='qui'),
    path('formulario/',formulario,name='for'),
    path('admin_obra/',admin_obra,name='ADMIN_OBR'),
    path('ficha_obr/<id>/',ficha_obra,name='FICHA_OBRA'),
    path('buscar_nombre/',buscar_nombre,name='BUSCAR_NOMBRE'),
    path('buscar_descripcion/',buscar_descripcion,name='BUSCAR_DESCRIPCION'),
    path('buscar_categoria/<id>/',buscar_categoria,name='BUSCAR_CAT'),
    path('registrar_colaborador/',registro_colaborador,name='RC'),
    path('logout/',cerrar,name='LOGOUT')
    
    
]
