
from rest_framework import serializers
from Entrenamiento.models import Entrenamiento

class EntrenamientoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Entrenamiento
        fields = '__all__'
