
from django.contrib import admin
from .models import Cliente, CuentaBancaria, Transaccion

admin.site.register(Cliente)
admin.site.register(CuentaBancaria)
admin.site.register(Transaccion)
