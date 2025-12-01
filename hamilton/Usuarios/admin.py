from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Usuario, Rol, DatosPaciente


@admin.register(Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'activo', 'created_at']
    list_filter = ['activo', 'nombre']
    search_fields = ['nombre', 'descripcion']


class DatosPacienteInline(admin.StackedInline):
    model = DatosPaciente
    can_delete = False
    verbose_name_plural = 'Datos de Paciente'


@admin.register(Usuario)
class UsuarioAdmin(BaseUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'rol', 'activo']
    list_filter = ['activo', 'rol', 'genero', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-created_at']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'email', 'telefono', 'fecha_nacimiento')}),
        ('Catálogos', {'fields': ('genero', 'edad', 'escolaridad', 'ocupacion')}),
        ('Rol y Permisos', {'fields': ('rol', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Información Profesional', {'fields': ('cedula_profesional', 'especialidad')}),
        ('Estado', {'fields': ('activo',)}),
        ('Fechas Importantes', {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'rol'),
        }),
    )
    
    readonly_fields = ['created_at', 'updated_at']
    
    def get_inline_instances(self, request, obj=None):
        if obj and hasattr(obj, 'rol') and obj.is_paciente:
            return [inline(self.model, self.admin_site) for inline in self.inlines]
        return []
    
    inlines = [DatosPacienteInline]


@admin.register(DatosPaciente)
class DatosPacienteAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'nombre_responsable', 'telefono_responsable', 'activo']
    list_filter = ['activo', 'parentesco_responsable']
    search_fields = ['usuario__username', 'usuario__email', 'nombre_responsable']
    raw_id_fields = ['usuario']
