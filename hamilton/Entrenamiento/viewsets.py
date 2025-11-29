from rest_framework import viewsets
from Entrenamiento.models import Entrenamiento
from Entrenamiento.serializer import EntrenamientoSerializers

class EntrenamientoViewsets(viewsets.ModelViewSet):
    queryset = Entrenamiento.objects.all()
    serializer_class = EntrenamientoSerializers