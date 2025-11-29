from rest_framework import serializers
from Catalogos.models import Categorias, Opciones, Generos, Preguntas, SepoMex, Edades, Escolaridad, Ocupacion, Parentesco

class CategoriasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'

class OpcionesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Opciones
        fields = '__all__'

class GenerosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Generos
        fields = '__all__'

class PreguntasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Preguntas
        fields = '__all__'

class SepoMexSerializers(serializers.ModelSerializer):
    class Meta:
        model = SepoMex
        fields = '__all__'


class EdadesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Edades
        fields = '__all__'


class EscolaridadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Escolaridad
        fields = '__all__'

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = '__all__'


class ParentescoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Parentesco
        fields = '__all__'