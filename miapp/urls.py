from django.urls import path
from .views import (
    raiz,
    crear_cliente,
    crear_cuenta,
    realizar_transaccion,
    cliente_lista,
    cuenta_lista,
    transaccion_lista,
    editar_cliente,
    eliminar_cliente,
)

urlpatterns = [
    path('', raiz, name='raiz'),
    path('crear-cliente/', crear_cliente, name='crear_cliente'),
    path('crear-cuenta/', crear_cuenta, name='crear_cuenta'),
    path('realizar-transaccion/', realizar_transaccion, name='realizar_transaccion'),
    path('clientes/', cliente_lista, name='cliente_lista'),
    path('cuentas/', cuenta_lista, name='cuenta_lista'),
    path('transacciones/', transaccion_lista, name='transaccion_lista'),
    path('editar-cliente/<int:pk>/', editar_cliente, name='editar_cliente'),
    path('eliminar-cliente/<int:pk>/', eliminar_cliente, name='eliminar_cliente'),
]
