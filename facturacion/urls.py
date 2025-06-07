# facturacion/urls.py
from django.urls import path
#from . import views
from .views import login_view, menu_principal, crear_factura, ver_facturas, clientes, configuracion, registro_view



urlpatterns = [
    path('login/', login_view, name='login'),
    path('registro/', registro_view, name='registro'),
    path('menu/', menu_principal, name='menu'),
    path('crear-factura/', crear_factura, name='crear_factura'),
    path('ver-facturas/', ver_facturas, name='ver_facturas'),
    path('clientes/', clientes, name='clientes'),
    path('configuracion/', configuracion, name='configuracion'),
]
