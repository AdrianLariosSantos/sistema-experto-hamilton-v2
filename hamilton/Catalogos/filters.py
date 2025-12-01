import django_filters
from django.db.models import Q

from Catalogos.models import (
    Categorias, 
    Edades, 
    Escolaridad, 
    Generos, 
    Ocupacion, 
    Opciones, 
    Parentesco, 
    Preguntas, 
    SepoMex
)

class CategoriasFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    categoria = django_filters.CharFilter(field_name='categoria', lookup_expr='icontains')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Categorias
        fields = ['categoria', 'descripcion', 'activo']

class EdadesFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Edades
        fields = ['descripcion', 'activo']

class EscolaridadFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Escolaridad
        fields = ['descripcion', 'activo']

class GenerosFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Generos
        fields = ['descripcion', 'activo']

class OcupacionFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Ocupacion
        fields = ['descripcion', 'activo']

class OpcionesFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    pregunta = django_filters.NumberFilter(field_name='pregunta')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Opciones
        fields = ['pregunta', 'descripcion', 'activo']

class ParentescoFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Parentesco
        fields = ['descripcion', 'activo']

class PreguntasFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    categoria = django_filters.NumberFilter(field_name='categoria')
    pregunta = django_filters.CharFilter(field_name='pregunta', lookup_expr='icontains')
    tipo = django_filters.CharFilter(field_name='tipo', lookup_expr='icontains')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = Preguntas
        fields = ['categoria', 'pregunta', 'tipo', 'activo']

class SepoMexFilter(django_filters.FilterSet):
    id = django_filters.NumberFilter(field_name='id')
    d_codigo = django_filters.CharFilter(field_name='d_codigo', lookup_expr='icontains')
    d_asenta = django_filters.CharFilter(field_name='d_asenta', lookup_expr='icontains')
    d_tipo_asenta = django_filters.CharFilter(field_name='d_tipo_asenta', lookup_expr='icontains')
    d_mnpio = django_filters.CharFilter(field_name='d_mnpio', lookup_expr='icontains')
    d_estado = django_filters.CharFilter(field_name='d_estado', lookup_expr='icontains')
    d_ciudad = django_filters.CharFilter(field_name='d_ciudad', lookup_expr='icontains')
    d_CP = django_filters.CharFilter(field_name='d_CP', lookup_expr='exact')
    activo = django_filters.BooleanFilter(field_name='activo')
    
    class Meta:
        model = SepoMex
        fields = ['d_codigo', 
                  'd_asenta', 
                  'd_tipo_asenta', 
                  'd_mnpio', 
                  'd_estado', 
                  'd_ciudad', 
                  'd_CP', 
                  'activo']