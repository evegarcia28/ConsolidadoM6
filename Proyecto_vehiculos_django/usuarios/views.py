from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .forms import RegistroForm

# Create your views here.
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()  # Guardamos el usuario
            group = Group.objects.get(name='visualizar_catalogo')  # Buscamos el grupo
            user.groups.add(group)  # Asignamos el usuario al grupo
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            return redirect('login')
    else:
        form = RegistroForm()
        return render(request, 'usuarios/registro.html', {'form':form})  