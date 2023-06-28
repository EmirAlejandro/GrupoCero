
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    path('', index,name='ind'),
    path('galeria/',galeria,name='gal'),
    path('login/',login_vista,name='LOGIN'),
    path('Registro/',Registro,name='reg'),
    path('quienes/',quienes,name='qui'),
    path('formulario/',formulario,name='for'),
    path('admin_obra/', login_required(permission_required(['webGrupoCero.add_obra','webGrupoCero.change_obra','webGrupoCero.delete_obra','webGrupoCero.view_obra'], login_url='/login/')(admin_obra)), name='ADMIN_OBR'),
    path('ficha_obr/<id>/',ficha_obra,name='FICHA_OBRA'),
    path('buscar_nombre/',buscar_nombre,name='BUSCAR_NOMBRE'),
    path('buscar_descripcion/',buscar_descripcion,name='BUSCAR_DESCRIPCION'),
    path('buscar_categoria/<id>/',buscar_categoria,name='BUSCAR_CAT'),
    path('registrar_colaborador/',registro_colaborador,name='RC'),
    path('logout/',cerrar,name='LOGOUT'),
    path('eliminar/<id>/',login_required(permission_required(['webGrupoCero.delete_obra'], login_url='/login/')(eliminar)),name='ELI'),
    path('modificar/<id>/',login_required(permission_required(['webGrupoCero.change_obra'], login_url='/login/')(modificar)),name='MOD'),
    path('modificar_obra/',login_required(permission_required(['webGrupoCero.change_obra'], login_url='/login/')(modificar_obra)),name='MO'),
    path('subir/',login_required(permission_required(['webGrupoCero.add_galeria'], login_url='/login/')(subir_galeria)),name='SG'),
    path('agregar/<articulo_id>/', agregar_articulo, name='AA'),
    path('carrito/',carrito, name='carrito'),
]

