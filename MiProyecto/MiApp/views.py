from django.shortcuts import render, redirect
from .forms import ClienteForm, CuentaBancariaForm, TransaccionForm, BusquedaForm
from .models import Cliente, CuentaBancaria, Transaccion

def insertar_datos(request):
    if request.method == 'POST': # definimos que el usuario va a enviarnos datos osea POST
        cliente_form = ClienteForm(request.POST)
        cuenta_form = CuentaBancariaForm(request.POST)
        transaccion_form = TransaccionForm(request.POST)

        if cliente_form.is_valid() and cuenta_form.is_valid() and transaccion_form.is_valid():
            cliente = cliente_form.save()
            cuenta_form.cleaned_data['cliente'] = cliente
            cuenta = cuenta_form.save()
            transaccion = transaccion_form.save(commit=False)
            transaccion.Cuenta_origen = cuenta
            transaccion.Cuenta_destino = cuenta  # Aquí debes ajustar según tu lógica
            transaccion.save()

            return redirect('insertar_datos')  # Puedes redirigir a donde desees

    else:
        cliente_form = ClienteForm()
        cuenta_form = CuentaBancariaForm()
        transaccion_form = TransaccionForm()

    return render(request, 'insertar_datos.html', {'cliente_form': cliente_form, 'cuenta_form': cuenta_form, 'transaccion_form': transaccion_form})


def buscar_datos(request):
    if request.method == 'POST':
        busqueda_form = BusquedaForm(request.POST)
        if busqueda_form.is_valid():
            termino_busqueda = busqueda_form.cleaned_data['termino_busqueda']

            # Realiza la lógica de búsqueda según tus necesidades
            resultados = Cliente.objects.filter(Nombre__icontains=termino_busqueda)

            return render(request, 'resultados_busqueda.html', {'resultados': resultados, 'termino_busqueda': termino_busqueda})

    else:
        busqueda_form = BusquedaForm()

    return render(request, 'buscar_datos.html', {'busqueda_form': busqueda_form})