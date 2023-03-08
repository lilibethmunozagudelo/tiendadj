from django.urls import path

from clientes.views import *

urlpatterns = [
    path('clientes/',clientes,name='clientes')
]