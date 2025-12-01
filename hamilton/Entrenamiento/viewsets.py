from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from helpers.exceptions import BadRequest, NotFound
from helpers.errors import error
from helpers.responses import ok_response, created_response

from Entrenamiento.models import Entrenamiento
from Entrenamiento.serializer import (
    EntrenamientoSerializer,
    EntrenamientoListSerializer,
    EntrenamientoCreateSerializer,
    EntrenamientoUpdateSerializer
)
from Usuarios.permissions import IsAdministrativo, IsPsicologo, IsAdministrativoOrPsicologo


class EntrenamientoViewsets(viewsets.ModelViewSet):
    """ViewSet para Evaluaciones/Entrenamiento"""
    queryset = Entrenamiento.objects.filter(activo=True)
    serializer_class = EntrenamientoListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['paciente', 'Genero', 'Edad', 'Clase', 'activo']
    
    def get_serializer_class(self):
        serial = {
            "list": EntrenamientoListSerializer,
            "retrieve": EntrenamientoSerializer,
            "create": EntrenamientoCreateSerializer,
            "update": EntrenamientoUpdateSerializer,
            "partial_update": EntrenamientoUpdateSerializer
        }
        return serial.get(self.action, self.serializer_class)
    
    def get_queryset(self):
        user = self.request.user
        
        # Administrativos y Psicólogos ven todas las evaluaciones
        if user.is_administrativo or user.is_psicologo:
            return Entrenamiento.objects.all()
        
        # Pacientes solo ven sus propias evaluaciones
        elif user.is_paciente:
            return Entrenamiento.objects.filter(paciente=user)
        
        return Entrenamiento.objects.none()
    
    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('-created_at'))
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        data = self.get_paginated_response(serializer.data).data
        return ok_response(data=data)
    
    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return ok_response(data=serializer.data)
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        # Solo administrativos y psicólogos pueden crear evaluaciones
        if not (request.user.is_administrativo or request.user.is_psicologo):
            raise BadRequest({'detail': 'No tiene permisos para crear evaluaciones'})
        
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            new_error = error(default_errors=serializer.errors)
            raise BadRequest(new_error)
        serializer.save()
        return created_response(data=serializer.data)
    
    @transaction.atomic
    def update(self, request, *args, **kwargs):
        # Solo administrativos y psicólogos pueden editar evaluaciones
        if not (request.user.is_administrativo or request.user.is_psicologo):
            raise BadRequest({'detail': 'No tiene permisos para editar evaluaciones'})
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if not serializer.is_valid():
            new_error = error(default_errors=serializer.errors)
            raise BadRequest(new_error)
        serializer.save()
        return ok_response(data=serializer.data)
    
    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)
    
    @transaction.atomic
    def destroy(self, request, *args, **kwargs):
        # Solo administrativos pueden eliminar evaluaciones
        if not request.user.is_administrativo:
            raise BadRequest({'detail': 'No tiene permisos para eliminar evaluaciones'})
        
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Evaluación desactivada correctamente")
    
    @action(detail=False, methods=['get'], permission_classes=[IsAdministrativoOrPsicologo])
    def por_paciente(self, request):
        """Obtener evaluaciones filtradas por paciente"""
        paciente_id = request.query_params.get('paciente_id')
        
        if not paciente_id:
            raise BadRequest({'detail': 'Se requiere el ID del paciente'})
        
        queryset = self.get_queryset().filter(paciente_id=paciente_id).order_by('-created_at')
        page = self.paginate_queryset(queryset)
        serializer = EntrenamientoListSerializer(page, many=True)
        data = self.get_paginated_response(serializer.data).data
        return ok_response(data=data)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def mis_evaluaciones(self, request):
        """Obtener evaluaciones del usuario autenticado (solo pacientes)"""
        if not request.user.is_paciente:
            raise BadRequest({'detail': 'Esta acción es solo para pacientes'})
        
        queryset = Entrenamiento.objects.filter(paciente=request.user, activo=True).order_by('-created_at')
        page = self.paginate_queryset(queryset)
        serializer = EntrenamientoListSerializer(page, many=True)
        data = self.get_paginated_response(serializer.data).data
        return ok_response(data=data)
    
    @action(detail=False, methods=['get'], permission_classes=[IsAdministrativoOrPsicologo])
    def estadisticas(self, request):
        """Obtener estadísticas de evaluaciones"""
        queryset = self.get_queryset()
        
        total = queryset.count()
        por_clase = queryset.values('Clase').annotate(total=models.Count('id'))
        por_genero = queryset.values('Genero__descripcion').annotate(total=models.Count('id'))
        por_edad = queryset.values('Edad__descripcion').annotate(total=models.Count('id'))
        
        data = {
            'total_evaluaciones': total,
            'por_clase': list(por_clase),
            'por_genero': list(por_genero),
            'por_edad': list(por_edad),
        }
        
        return ok_response(data=data)
