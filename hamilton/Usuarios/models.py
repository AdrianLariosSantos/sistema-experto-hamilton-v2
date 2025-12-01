from django.db import models
from django.contrib.auth.models import AbstractUser
from Catalogos.models import Generos, Edades, Escolaridad, Ocupacion, Parentesco


class Rol(models.Model):
    """Modelo para los roles del sistema"""
    ADMINISTRATIVO = 'administrativo'
    PSICOLOGO = 'psicologo'
    PACIENTE = 'paciente'
    
    ROLES_CHOICES = [
        (ADMINISTRATIVO, 'Administrativo'),
        (PSICOLOGO, 'Psicólogo'),
        (PACIENTE, 'Paciente'),
    ]
    
    nombre = models.CharField(max_length=50, choices=ROLES_CHOICES, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'cat_roles'
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'
    
    def __str__(self):
        return self.get_nombre_display()


class Usuario(AbstractUser):
    """Modelo extendido de usuario"""
    email = models.EmailField('Email', unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    
    # Relaciones con catálogos
    genero = models.ForeignKey(Generos, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')
    edad = models.ForeignKey(Edades, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')
    escolaridad = models.ForeignKey(Escolaridad, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')
    ocupacion = models.ForeignKey(Ocupacion, on_delete=models.SET_NULL, null=True, blank=True, related_name='usuarios')
    
    # Rol del usuario
    rol = models.ForeignKey(Rol, on_delete=models.PROTECT, related_name='usuarios')
    
    # Campos adicionales
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Para psicólogos
    cedula_profesional = models.CharField(max_length=50, blank=True, null=True)
    especialidad = models.CharField(max_length=200, blank=True, null=True)
    
    class Meta:
        db_table = 'usuarios'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
    
    def __str__(self):
        return f"{self.username} - {self.get_full_name()}"
    
    @property
    def is_administrativo(self):
        return self.rol.nombre == Rol.ADMINISTRATIVO
    
    @property
    def is_psicologo(self):
        return self.rol.nombre == Rol.PSICOLOGO
    
    @property
    def is_paciente(self):
        return self.rol.nombre == Rol.PACIENTE


class DatosPaciente(models.Model):
    """Datos adicionales específicos para pacientes"""
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='datos_paciente')
    
    # Información familiar
    parentesco_responsable = models.ForeignKey(Parentesco, on_delete=models.SET_NULL, null=True, blank=True, related_name='pacientes')
    nombre_responsable = models.CharField(max_length=200, blank=True, null=True)
    telefono_responsable = models.CharField(max_length=15, blank=True, null=True)
    
    # Información médica
    alergias = models.TextField(blank=True, null=True)
    medicamentos_actuales = models.TextField(blank=True, null=True)
    antecedentes_medicos = models.TextField(blank=True, null=True)
    
    # Control
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'datos_pacientes'
        verbose_name = 'Datos de Paciente'
        verbose_name_plural = 'Datos de Pacientes'
    
    def __str__(self):
        return f"Datos de {self.usuario.get_full_name()}"
