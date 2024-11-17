from django.shortcuts import render, redirect
from .models import Vehiculo
from .forms import VehiculoForm
from django.contrib.auth.decorators import login_required, permission_required

# Vista principal
def index(request):
    contexto = {
        'puede_agregar_vehiculos': request.user.has_perm('vehiculo.add_vehiculo'),
    }
    return render(request, 'vehiculo/index.html', contexto)

# Vista para listar vehículos
@login_required()
@permission_required('vehiculo.view_vehiculo', raise_exception=True)
def listar_vehiculos(request):
        vehiculos = Vehiculo.objects.all()
        contexto = {
        'vehiculos': vehiculos,
        'puede_agregar_vehiculos': request.user.has_perm('vehiculo.add_vehiculo'),
    }
        return render(request, 'vehiculo/listar_vehiculos.html', contexto)
    

# Vista para agregar un vehículo
@login_required()
@permission_required('vehiculo.add_vehiculo', raise_exception=True)
def agregar_vehiculo(request):
    contexto = {
        'puede_agregar_vehiculos': request.user.has_perm('vehiculo.add_vehiculo'),
    }
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vehiculo:listar_vehiculos')
    else:
        form = VehiculoForm()
    
    contexto['form'] = form
    return render(request, 'vehiculo/agregar_vehiculo.html', contexto)    