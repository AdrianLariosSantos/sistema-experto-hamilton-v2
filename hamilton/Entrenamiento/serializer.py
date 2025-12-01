from rest_framework import serializers
from Entrenamiento.models import Entrenamiento


class EntrenamientoSerializer(serializers.ModelSerializer):
    """Serializer base para Entrenamiento"""
    paciente_nombre = serializers.SerializerMethodField()
    genero_nombre = serializers.CharField(source='Genero.descripcion', read_only=True)
    edad_nombre = serializers.CharField(source='Edad.descripcion', read_only=True)
    
    class Meta:
        model = Entrenamiento
        fields = '__all__'
        read_only_fields = ['created_at', 'updated_at']
    
    def get_paciente_nombre(self, obj):
        if obj.paciente:
            return obj.paciente.get_full_name() or obj.paciente.username
        return None


class EntrenamientoListSerializer(serializers.ModelSerializer):
    """Serializer para listar evaluaciones"""
    paciente_nombre = serializers.SerializerMethodField()
    genero_nombre = serializers.CharField(source='Genero.descripcion', read_only=True)
    edad_nombre = serializers.CharField(source='Edad.descripcion', read_only=True)
    
    class Meta:
        model = Entrenamiento
        fields = [
            'id', 'paciente', 'paciente_nombre', 'Genero', 'genero_nombre',
            'Edad', 'edad_nombre', 'Clase', 'activo', 'created_at'
        ]
    
    def get_paciente_nombre(self, obj):
        if obj.paciente:
            return obj.paciente.get_full_name() or obj.paciente.username
        return None


class EntrenamientoCreateSerializer(serializers.ModelSerializer):
    """Serializer para crear evaluaciones"""
    class Meta:
        model = Entrenamiento
        fields = [
            'paciente', 'Genero', 'Edad', 'Humor', 'Culpa', 'Suicidio',
            'IPrecoz', 'IIntermedio', 'ITardio', 'Trabajo', 'Inhibicion',
            'Agitacion', 'APsiquica', 'ASomatica', 'SGastrointestinales',
            'SGenerales', 'SGenitales', 'Hipocondria', 'Peso', 'Introspeccion',
            'AnimoAnsioso', 'Tension', 'Temores', 'Insomnio', 'Intelectual',
            'AnimoDeprimido', 'SomaticosMusculares', 'SomaticosSensoriales',
            'Cardiovasculares', 'Respiratorios', 'Gastrointestinales',
            'Genitourinarios', 'Autonomos', 'Clase'
        ]
        extra_kwargs = {
            'Genero': {'required': True},
            'Edad': {'required': True},
        }


class EntrenamientoUpdateSerializer(serializers.ModelSerializer):
    """Serializer para actualizar evaluaciones"""
    class Meta:
        model = Entrenamiento
        fields = [
            'Humor', 'Culpa', 'Suicidio', 'IPrecoz', 'IIntermedio', 'ITardio',
            'Trabajo', 'Inhibicion', 'Agitacion', 'APsiquica', 'ASomatica',
            'SGastrointestinales', 'SGenerales', 'SGenitales', 'Hipocondria',
            'Peso', 'Introspeccion', 'AnimoAnsioso', 'Tension', 'Temores',
            'Insomnio', 'Intelectual', 'AnimoDeprimido', 'SomaticosMusculares',
            'SomaticosSensoriales', 'Cardiovasculares', 'Respiratorios',
            'Gastrointestinales', 'Genitourinarios', 'Autonomos', 'Clase', 'activo'
        ]


# Mantener compatibilidad con código anterior
class EntrenamientoSerializers(EntrenamientoSerializer):
    pass

