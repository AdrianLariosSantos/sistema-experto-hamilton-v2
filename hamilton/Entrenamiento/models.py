from django.db import models
from Catalogos.models import Generos, Edades 

# Create your models here.
class Entrenamiento(models.Model):
    Genero =  models.ForeignKey(Generos, on_delete=models.CASCADE, related_name='generos')
    Edad = models.ForeignKey(Edades, on_delete=models.CASCADE, related_name='edades')
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
    Clase = models.CharField(max_length=150, blank=True, null=True)


    class Meta:
        db_table = 'entrenamiento'