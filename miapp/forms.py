from django import forms
from .models import Cliente, CuentaBancaria, Transaccion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

class CuentaBancariaForm(forms.ModelForm):
    class Meta:
        model = CuentaBancaria
        fields = '__all__'

class TransaccionForm(forms.ModelForm):
    class Meta:
        model = Transaccion
        fields = '__all__'
