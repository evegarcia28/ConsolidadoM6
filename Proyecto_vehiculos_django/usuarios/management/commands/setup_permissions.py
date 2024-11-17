from django.contrib.auth.models import User, Group, Permission
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help= "Configura el usuario Admin, los grupos de permisos y los permisos iniciales"
    
    def handle(self, *args, **kwargs):
#crear usuario admin con permisos completos
        admin_user, created =  User.objects.get_or_create(
            username='admin', defaults={'email':'admin@admin.com', 'is_staff': True, 'is_superuser': True})
        
        if created:
            admin_user.set_password('admin')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('Usuario admin creado con exito'))
        else:
            self.stdout.write(self.style.WARNING('El usuario admin ya existe'))
            
        #Crear los grupos de usuario
        grupos_permisos= {'add_vehiculomodel': ['add_vehiculo', 'view_vehiculo'], 
                        'visualizar_catalogo': ['view_vehiculo']}
        
        for grupo_nombre, permisos in grupos_permisos.items():
            grupo, creado = Group.objects.get_or_create(name=grupo_nombre)
            
            if creado:
                self.stdout.write(self.style.SUCCESS(f'Grupo {grupo_nombre} creado y permisos asignados con éxito'))
            else:
                self.stdout.write(self.style.WARNING(f'Grupo {grupo_nombre} ya existe'))
                
                
            for permiso_codename in permisos:
                try:
                    permiso = Permission.objects.get(codename=permiso_codename)
                    grupo.permissions.add(permiso)
                    self.stdout.write(self.style.SUCCESS(f'Permiso "{permiso_codename}" asignado al grupo "{grupo_nombre}"'))
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permiso "{permiso_codename}" no encontrado'))
        
        