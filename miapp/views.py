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