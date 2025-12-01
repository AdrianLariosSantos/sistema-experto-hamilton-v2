from django.db import models
from Catalogos.models import Generos, Edades 
from django.conf import settings

# Create your models here.
class Entrenamiento(models.Model):
    # Relación con el paciente (usuario)
    paciente = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='evaluaciones',
        null=True,
        blank=True,
        limit_choices_to={'rol__nombre': 'paciente'}
    )
    
    # Catálogos
    Genero = models.ForeignKey(Generos, on_delete=models.CASCADE, related_name='evaluaciones_genero')
    Edad = models.ForeignKey(Edades, on_delete=models.CASCADE, related_name='evaluaciones_edad')
    
    # Preguntas de Hamilton para Depresión
    Humor = models.IntegerField(null=True, blank=True)
    Culpa = models.IntegerField(null=True, blank=True)
    Suicidio = models.IntegerField(null=True, blank=True)
    IPrecoz = models.IntegerField(null=True, blank=True)
    IIntermedio = models.IntegerField(null=True, blank=True)
    ITardio = models.IntegerField(null=True, blank=True)
    Trabajo = models.IntegerField(null=True, blank=True)
    Inhibicion = models.IntegerField(null=True, blank=True)
    Agitacion = models.IntegerField(null=True, blank=True)
    APsiquica = models.IntegerField(null=True, blank=True)
    ASomatica = models.IntegerField(null=True, blank=True)
    SGastrointestinales = models.IntegerField(null=True, blank=True)
    SGenerales = models.IntegerField(null=True, blank=True)
    SGenitales = models.IntegerField(null=True, blank=True)
    Hipocondria = models.IntegerField(null=True, blank=True)
    Peso = models.IntegerField(null=True, blank=True)
    Introspeccion = models.IntegerField(null=True, blank=True)
    
    # Preguntas de Hamilton para Ansiedad
    AnimoAnsioso = models.IntegerField(null=True, blank=True)
    Tension = models.IntegerField(null=True, blank=True)
    Temores = models.IntegerField(null=True, blank=True)
    Insomnio = models.IntegerField(null=True, blank=True)
    Intelectual = models.IntegerField(null=True, blank=True)
    AnimoDeprimido = models.IntegerField(null=True, blank=True)
    SomaticosMusculares = models.IntegerField(null=True, blank=True)
    SomaticosSensoriales = models.IntegerField(null=True, blank=True)
    Cardiovasculares = models.IntegerField(null=True, blank=True)
    Respiratorios = models.IntegerField(null=True, blank=True)
    Gastrointestinales = models.IntegerField(null=True, blank=True)
    Genitourinarios = models.IntegerField(null=True, blank=True)
    Autonomos = models.IntegerField(null=True, blank=True)
    
    # Resultado de la evaluación
    Clase = models.CharField(max_length=150, blank=True, null=True)
    
    # Campos de control
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'entrenamiento'
        verbose_name = 'Evaluación'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['-created_at']
    
    def __str__(self):
        paciente_nombre = self.paciente.get_full_name() if self.paciente else "Sin asignar"
        return f"Evaluación de {paciente_nombre} - {self.Clase} ({self.created_at.strftime('%d/%m/%Y')})"