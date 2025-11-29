from rest_framework import viewsets
from Catalogos.models import Categorias, Generos, Opciones, Preguntas, SepoMex, Edades, Escolaridad, Ocupacion, Parentesco
from Catalogos.serializers import CategoriasSerializers, OpcionesSerializers, GenerosSerializers, PreguntasSerializers, SepoMexSerializers, EdadesSerializers, EscolaridadSerializers, OcupacionSerializers, ParentescoSerializers

class CategoriasViewsets(viewsets.ModelViewSet):
    queryset = Categorias.objects.filter(activo=True)
    serializer_class = CategoriasSerializers

class GenerosViewsets(viewsets.ModelViewSet):
    queryset = Generos.objects.filter(activo=True)
    serializer_class = GenerosSerializers

class OpcionesViewsets(viewsets.ModelViewSet):
    queryset = Opciones.objects.filter(activo=True)
    serializer_class = OpcionesSerializers


class PreguntasViewsets(viewsets.ModelViewSet):
    queryset = Preguntas.objects.filter(activo=True)
    serializer_class = PreguntasSerializers

class SepoMexViewsets(viewsets.ModelViewSet):
    queryset = SepoMex.objects.all()
    serializer_class = SepoMexSerializers

class EdadesViewsets(viewsets.ModelViewSet):
    queryset = Edades.objects.all()
    serializer_class = EdadesSerializers

class EscolaridadViewsets(viewsets.ModelViewSet):
    queryset = Escolaridad.objects.all()
    serializer_class = EscolaridadSerializers
class OcupacionViewsets(viewsets.ModelViewSet):
    queryset = Ocupacion.objects.all()
    serializer_class = OcupacionSerializers
    
class ParentescoViewsets(viewsets.ModelViewSet):
    queryset = Parentesco.objects.all()
    serializer_class = ParentescoSerializers