from rest_framework import viewsets
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import F, Q, Max, Count
from django.db import transaction
from helpers.exceptions import BadRequest, NotFound
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import action

from helpers.errors import error

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

from Catalogos.serializers import (
    CategoriasSerializers,
    CategoriasListSerializers,
    CategoriasCreateSerializers,
    OpcionesSerializers,
    OpcionesListSerializers,
    OpcionesCreateSerializers,
    GenerosSerializers,
    GenerosListSerializers,
    GenerosCreateSerializers,
    PreguntasSerializers,
    PreguntasListSerializers,
    PreguntasCreateSerializers,
    SepoMexSerializers,
    SepoMexListSerializers,
    SepoMexCreateSerializers,
    EdadesSerializers,
    EdadesListSerializers,
    EdadesCreateSerializers,
    EscolaridadSerializers,
    EscolaridadListSerializers,
    EscolaridadCreateSerializers,
    OcupacionSerializers,
    OcupacionListSerializers,
    OcupacionCreateSerializers,
    ParentescoSerializers,
    ParentescoListSerializers,
    ParentescoCreateSerializers
)

from helpers.responses import (
    ok_response, 
    created_response,
    not_found_response,
    bad_request_response,
    no_unauthorized_response,
    no_content_response
)


# ViewSet para Categorias
class CategoriasViewsets(viewsets.ModelViewSet):
    queryset = Categorias.objects.filter(activo=True)
    serializer_class = CategoriasListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": CategoriasListSerializers,
            "retrieve": CategoriasSerializers,
            "create": CategoriasCreateSerializers,
            "update": CategoriasCreateSerializers,
            "partial_update": CategoriasCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Categorias.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")


# ViewSet para Generos
class GenerosViewsets(viewsets.ModelViewSet):
    queryset = Generos.objects.filter(activo=True)
    serializer_class = GenerosListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": GenerosListSerializers,
            "retrieve": GenerosSerializers,
            "create": GenerosCreateSerializers,
            "update": GenerosCreateSerializers,
            "partial_update": GenerosCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Generos.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")


# ViewSet para Opciones
class OpcionesViewsets(viewsets.ModelViewSet):
    queryset = Opciones.objects.filter(activo=True)
    serializer_class = OpcionesListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": OpcionesListSerializers,
            "retrieve": OpcionesSerializers,
            "create": OpcionesCreateSerializers,
            "update": OpcionesCreateSerializers,
            "partial_update": OpcionesCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Opciones.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")


# ViewSet para Preguntas
class PreguntasViewsets(viewsets.ModelViewSet):
    queryset = Preguntas.objects.filter(activo=True)
    serializer_class = PreguntasListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": PreguntasListSerializers,
            "retrieve": PreguntasSerializers,
            "create": PreguntasCreateSerializers,
            "update": PreguntasCreateSerializers,
            "partial_update": PreguntasCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Preguntas.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('orden'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")


# ViewSet para SepoMex
class SepoMexViewsets(viewsets.ModelViewSet):
    queryset = SepoMex.objects.all()
    serializer_class = SepoMexListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": SepoMexListSerializers,
            "retrieve": SepoMexSerializers,
            "create": SepoMexCreateSerializers,
            "update": SepoMexCreateSerializers,
            "partial_update": SepoMexCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.delete()
        return ok_response(None, message="Registro eliminado correctamente")


# ViewSet para Edades
class EdadesViewsets(viewsets.ModelViewSet):
    queryset = Edades.objects.filter(activo=True)
    serializer_class = EdadesListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": EdadesListSerializers,
            "retrieve": EdadesSerializers,
            "create": EdadesCreateSerializers,
            "update": EdadesCreateSerializers,
            "partial_update": EdadesCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Edades.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")


# ViewSet para Escolaridad
class EscolaridadViewsets(viewsets.ModelViewSet):
    queryset = Escolaridad.objects.filter(activo=True)
    serializer_class = EscolaridadListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": EscolaridadListSerializers,
            "retrieve": EscolaridadSerializers,
            "create": EscolaridadCreateSerializers,
            "update": EscolaridadCreateSerializers,
            "partial_update": EscolaridadCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Escolaridad.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")


# ViewSet para Ocupacion
class OcupacionViewsets(viewsets.ModelViewSet):
    queryset = Ocupacion.objects.filter(activo=True)
    serializer_class = OcupacionListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": OcupacionListSerializers,
            "retrieve": OcupacionSerializers,
            "create": OcupacionCreateSerializers,
            "update": OcupacionCreateSerializers,
            "partial_update": OcupacionCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Ocupacion.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")


# ViewSet para Parentesco
class ParentescoViewsets(viewsets.ModelViewSet):
    queryset = Parentesco.objects.filter(activo=True)
    serializer_class = ParentescoListSerializers
    filter_backends = [DjangoFilterBackend]

    def get_serializer_class(self):
        serial = {
            "list": ParentescoListSerializers,
            "retrieve": ParentescoSerializers,
            "create": ParentescoCreateSerializers,
            "update": ParentescoCreateSerializers,
            "partial_update": ParentescoCreateSerializers
        }
        return serial.get(self.action, self.serializer_class)

    def get_queryset(self):
        return Parentesco.objects.filter(activo=True)

    def get_object(self):
        try:
            obj_id = self.kwargs.get('pk')
            obj = self.get_queryset().get(pk=obj_id)
            self.check_object_permissions(self.request, obj)
            return obj
        except ObjectDoesNotExist:
            raise NotFound()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset().order_by('id'))
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
        instance = self.get_object()
        instance.activo = False
        instance.save()
        return ok_response(None, message="Registro desactivado correctamente")