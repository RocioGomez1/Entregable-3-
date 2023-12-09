from django.db import models

class Cliente(models.Model):
    Nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    email = models.EmailField()
    Edad = models.IntegerField()

    def __str__(self):
        return self.Nombre

class CuentaBancaria(models.Model):
    cliente = models.ForeignKey("Cliente", on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    Numero_cuenta = models.CharField(max_length=20)

    def __str__(self):
        return f"Cuenta de {self.cliente.Nombre}"

class Transaccion(models.Model):
    Cuenta_origen = models.ForeignKey("CuentaBancaria", on_delete=models.CASCADE, related_name="transc_origen")
    Cuenta_destino = models.ForeignKey("CuentaBancaria", on_delete=models.CASCADE, related_name="transc_destino")
    Canal = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Transacción de {self.Cuenta_origen.cliente.Nombre} a {self.Cuenta_destino.cliente.Nombre}"
    
