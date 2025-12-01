from rest_framework import serializers
from Catalogos.models import (
    Categorias, 
    Opciones, 
    Generos, 
    Preguntas, 
    SepoMex, 
    Edades, 
    Escolaridad, 
    Ocupacion, 
    Parentesco)

class CategoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
        
class CategoriasListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

class CategoriasCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['descripcion', 'activo']
        extra_kwargs = {
            'descripcion': {'required': True},
            'activo': {'required': True},
        }

class OpcionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = '__all__'
        
class OpcionesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = '__all__'

class OpcionesCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = [ 'descripcion', 'activo']
        extra_kwargs = {
            'descripcion': {'required': True},
            'activo': {'required': True},
        }


class GenerosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'

class GenerosListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'

class GenerosCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = ['descripcion', 'activo']
        extra_kwargs = {
            'descripcion': {'required': True},
            'activo': {'required': True},
        }

class PreguntasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = '__all__'
        
class PreguntasListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = '__all__'
class PreguntasCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = ['orden', 'pregunta', 'descripcion', 'categoria', 'activo']
        extra_kwargs = {
            'orden': {'required': True},
            'pregunta': {'required': True},
            'descripcion': {'required': True},
            'categoria': {'required': True},
            'activo': {'required': True},
        }

class SepoMexSerializers(serializers.ModelSerializer):
    class Meta:
        model = SepoMex
        fields = '__all__'
        
class SepoMexListSerializers(serializers.ModelSerializer):
    class Meta:
        model = SepoMex
        fields = '__all__'

class SepoMexCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = SepoMex
        fields = ['d_codigo', 
                  'd_asenta', 
                  'd_tipo_asenta', 
                  'D_mnpio', 
                  'd_estado', 
                  'd_ciudad', 
                  'd_cp', 
                  'c_estado', 
                  'c_oficina', 
                  'c_cp', 
                  'c_tipo_asenta', 
                  'c_mnpio', 
                  'id_asenta_cpcons', 
                  'd_zona', 
                  'c_cve_ciudad'
                  ]
        extra_kwargs = {
            'd_codigo': {'required': True},
            'd_asenta': {'required': True},
            'd_tipo_asenta': {'required': True},
            'D_mnpio': {'required': True},
            'd_estado': {'required': True},
            'd_ciudad': {'required': True},
            'd_cp': {'required': True},
            'c_estado': {'required': True},
            'c_oficina': {'required': True},
            'c_cp': {'required': True},
            'c_tipo_asenta': {'required': True},
            'c_mnpio': {'required': True},
            'id_asenta_cpcons': {'required': True},
            'd_zona': {'required': True},
            'c_cve_ciudad': {'required': True},
        }


class EdadesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Edades
        fields = '__all__'
        
class EdadesListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Edades
        fields = '__all__'

class EdadesCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Edades
        fields = ['descripcion', 'activo']
        extra_kwargs = {
            'descripcion': {'required': True},
            'activo': {'required': True},
        }


class EscolaridadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Escolaridad
        fields = '__all__'

class EscolaridadListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Escolaridad
        fields = '__all__'
        
class EscolaridadCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Escolaridad
        fields = ['descripcion', 'activo']
        extra_kwargs = {
            'descripcion': {'required': True},
            'activo': {'required': True},
        }

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = '__all__'

class OcupacionListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = '__all__'

class OcupacionCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ['descripcion', 'activo']
        extra_kwargs = {
            'descripcion': {'required': True},
            'activo': {'required': True},
        }

class ParentescoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parentesco
        fields = '__all__'
        
class ParentescoListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parentesco
        fields = '__all__'

class ParentescoCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parentesco
        fields = ['descripcion', 'activo']
        extra_kwargs = {
            'descripcion': {'required': True},
            'activo': {'required': True},
        }