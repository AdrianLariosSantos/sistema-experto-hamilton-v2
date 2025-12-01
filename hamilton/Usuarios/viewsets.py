from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
from django.db import models

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from django_filters.rest_framework import DjangoFilterBackend

from helpers.exceptions import BadRequest, NotFound
from helpers.errors import error
from helpers.responses import ok_response, created_response

from .models import Usuario, Rol, DatosPaciente
from .serializers import (
    UsuarioSerializer,
    UsuarioListSerializer,
    UsuarioDetailSerializer,
    UsuarioCreateSerializer,
    UsuarioUpdateSerializer,
    ChangePasswordSerializer,
    LoginSerializer,
    RolSerializer
)
from .permissions import IsAdministrativo, IsPsicologo, IsPaciente

User = get_user_model()


class AuthViewSet(viewsets.GenericViewSet):
    """ViewSet para autenticación"""
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        """Login de usuario - Genera o retorna token existente"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            raise BadRequest({'detail': 'Credenciales inválidas'})
        
        if not user.activo:
            raise BadRequest({'detail': 'Usuario inactivo'})
        
        # Obtener o crear token
        token, created = Token.objects.get_or_create(user=user)
        
        # Obtener permisos y grupos
        permisos = list(user.get_all_permissions())
        grupos = list(user.groups.values_list('name', flat=True))
        nombre_completo = f'{user.first_name} {user.last_name}'.strip()
        
        # Actualizar last_login
        user.last_login = timezone.now()
        user.save()
        
        # Datos del usuario
        user_data = UsuarioDetailSerializer(user).data
        
        data = {
            'user': user_data,
            'token': token.key,
            'user_id': user.id,
            'nombre_completo': nombre_completo or user.username,
            'username': user.username,
            'email': user.email,
            'rol': user.rol.get_nombre_display() if hasattr(user, 'rol') else None,
            'is_superuser': user.is_superuser,
            'is_active': user.is_active,
            'grupos': grupos,
            'permisos': permisos,
        }
        
        return ok_response(data=data, message='Login exitoso')
    
    @action(detail=False, methods=['delete', 'post'], permission_classes=[IsAuthenticated])
    def logout(self, request):
        """Logout de usuario - Elimina el token"""
        try:
            # Eliminar el token del usuario
            Token.objects.filter(user=request.user).delete()
            return ok_response(message='Logout exitoso')
        except Exception as e:
            raise BadRequest({'detail': str(e)})
    
    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """Obtener datos del usuario autenticado"""
        serializer = UsuarioDetailSerializer(request.user)
        return ok_response(data=serializer.data)


class RolViewSet(viewsets.ModelViewSet):
    """ViewSet para Roles"""
    queryset = Rol.objects.filter(activo=True)
    serializer_class = RolSerializer
    permission_classes = [IsAuthenticated, IsAdministrativo]
    filter_backends = [DjangoFilterBackend]
    
    def get_queryset(self):
        return Rol.objects.filter(activo=True)
    
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('nombre'))
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        data = self.get_paginated_response(serializer.data).data if page else serializer.data
        return ok_response(data=data)


class UsuarioViewSet(viewsets.ModelViewSet):
    """ViewSet para Usuarios"""
    queryset = Usuario.objects.filter(activo=True)
    serializer_class = UsuarioListSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['rol', 'genero', 'edad', 'activo']
    
    def get_serializer_class(self):
        serial = {
            "list": UsuarioListSerializer,
            "retrieve": UsuarioDetailSerializer,
            "create": UsuarioCreateSerializer,
            "update": UsuarioUpdateSerializer,
            "partial_update": UsuarioUpdateSerializer
        }
        return serial.get(self.action, self.serializer_class)
    
    def get_queryset(self):
        user = self.request.user
        
        # Administrativos ven todos
        if user.is_administrativo:
            return Usuario.objects.all()
        
        # Psicólogos ven pacientes y a sí mismos
        elif user.is_psicologo:
            return Usuario.objects.filter(
                models.Q(rol__nombre='paciente') | models.Q(id=user.id)
            )
        
        # Pacientes solo se ven a sí mismos
        elif user.is_paciente:
            return Usuario.objects.filter(id=user.id)
        
        return Usuario.objects.none()
    
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
        # Solo administrativos pueden crear usuarios
        if not request.user.is_administrativo:
            raise BadRequest({'detail': 'No tiene permisos para crear usuarios'})
        
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            new_error = error(default_errors=serializer.errors)
            raise BadRequest(new_error)
        serializer.save()
        return created_response(data=serializer.data)
    
    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Usuarios solo pueden editarse a sí mismos, excepto administrativos
        if not request.user.is_administrativo and instance.id != request.user.id:
            raise BadRequest({'detail': 'No tiene permisos para editar este usuario'})
        
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
        # Solo administrativos pueden desactivar usuarios
        if not request.user.is_administrativo:
            raise BadRequest({'detail': 'No tiene permisos para desactivar usuarios'})
        
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Usuario desactivado correctamente")
    
    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        """Cambiar contraseña de usuario"""
        instance = self.get_object()
        
        # Solo el mismo usuario o un administrativo pueden cambiar la contraseña
        if instance.id != request.user.id and not request.user.is_administrativo:
            raise BadRequest({'detail': 'No tiene permisos para cambiar esta contraseña'})
        
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        if not serializer.is_valid():
            new_error = error(default_errors=serializer.errors)
            raise BadRequest(new_error)
        
        serializer.save()
        return ok_response(message='Contraseña actualizada correctamente')
    
    @action(detail=False, methods=['get'])
    def pacientes(self, request):
        """Listar solo pacientes"""
        queryset = self.get_queryset().filter(rol__nombre='paciente')
        page = self.paginate_queryset(queryset)
        serializer = UsuarioListSerializer(page, many=True)
        data = self.get_paginated_response(serializer.data).data
        return ok_response(data=data)
    
    @action(detail=False, methods=['get'])
    def psicologos(self, request):
        """Listar solo psicólogos"""
        if not request.user.is_administrativo:
            raise BadRequest({'detail': 'No tiene permisos para ver esta información'})
        
        queryset = self.get_queryset().filter(rol__nombre='psicologo')
        page = self.paginate_queryset(queryset)
        serializer = UsuarioListSerializer(page, many=True)
        data = self.get_paginated_response(serializer.data).data
        return ok_response(data=data)
