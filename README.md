# Proyecto Django - Registro Banco

Este proyecto se encarga de registrar datos de diferentes usuarios o clientes a los cuales
se les puede asignar un numero de cuenta y se pueden generar trasnsacciones entre usuarios.

## Instrucciones de Ejecución

1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv venv`.
3. Activa el entorno virtual: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Linux/Mac).
4. Instala las dependencias: `pip install -r requirements.txt`.
5. Aplica las migraciones: `python manage.py migrate`.
6. Ejecuta el servidor: `python manage.py runserver`.
   
## Detalle Proyecto

0. Instalar `django`:  `pip install django`
1. Crear carpeta para nuestro proyecto.
2. dentro de esa carpeta: `django-admin startproject {nombre_proyecto}`. Este comando dejará creada una nueva carpeta `{nombre_proyecto}`.
3. Ingresar dentro del proyecto en terminal `cd {nombre_proyecto}`.
4. Iniciar App Django `django-admin startapp {miapp}`.
5. Crear modelos :
  - Modelo Cliente: este modelo recolecta datos de los clientes.
  ```Bash
      class Cliente(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        nombre = models.CharField(max_length=50)
        dni = models.CharField(max_length=8)
        email = models.EmailField()
        edad = models.IntegerField()
    
        def __str__(self):
            return self.nombre
```
  - Modelo CuentaBancaria: este modelo recolecta la cuenta en funcion al cliente.
```Bash
class CuentaBancaria(models.Model):
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    numero_cuenta = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Cuenta de {self.cliente.nombre}"
```

  - Modelo Transaccion: este modelo recolecta data de la transaccion en funcion a la cuenta.
```Bash
class Transaccion(models.Model):
    cuenta = models.ForeignKey(CuentaBancaria, on_delete=models.CASCADE, related_name="transacciones")
    canal = models.CharField(max_length=50)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transacción de {self.cuenta.cliente.nombre}"

```


6. Creacion de Forms.py
```Bash   
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
```

7. creacion de Views:
```Bash
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Cliente, CuentaBancaria, Transaccion
from .forms import ClienteForm, CuentaBancariaForm, TransaccionForm

def raiz(request):
    mensaje_bienvenida = "Bienvenido a MiProyecto. Comienza a explorar las funciones."
    return render(request, 'miapp/bienvenida.html', {'mensaje': mensaje_bienvenida})


def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('raiz')  # Redirige a la lista de clientes después de guardar
    else:
        form = ClienteForm()

    return render(request, 'miapp/crear_cliente.html', {'form': form})

def crear_cuenta(request):
    if request.method == 'POST':
        form = CuentaBancariaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('miapp/cuenta_lista')
    else:
        form = CuentaBancariaForm()

    return render(request, 'miapp/crear_cuenta.html', {'form': form})

def realizar_transaccion(request):
    if request.method == 'POST':
        form = TransaccionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('miapp/transaccion_lista')
    else:
        form = TransaccionForm()

    return render(request, 'miapp/realizar_transaccion.html', {'form': form})

def cliente_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'miapp/cliente_lista.html', {'clientes': clientes})

def cuenta_lista(request):
    cuentas = CuentaBancaria.objects.all()
    return render(request, 'miapp/cuenta_lista.html', {'cuentas': cuentas})

def transaccion_lista(request):
    transacciones = Transaccion.objects.all()
    return render(request, 'miapp/transaccion_lista.html', {'transacciones': transacciones})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('miapp/cliente_lista')
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'miapp/editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    cliente.delete()
    return redirect('miapp/cliente_lista')
```
