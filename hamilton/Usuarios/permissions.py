from rest_framework import permissions


class IsAdministrativo(permissions.BasePermission):
    """
    Permiso personalizado para usuarios con rol Administrativo
    """
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'rol') and
            request.user.is_administrativo
        )


class IsPsicologo(permissions.BasePermission):
    """
    Permiso personalizado para usuarios con rol Psicólogo
    """
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'rol') and
            request.user.is_psicologo
        )


class IsPaciente(permissions.BasePermission):
    """
    Permiso personalizado para usuarios con rol Paciente
    """
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'rol') and
            request.user.is_paciente
        )


class IsAdministrativoOrPsicologo(permissions.BasePermission):
    """
    Permiso para Administrativos o Psicólogos
    """
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            hasattr(request.user, 'rol') and
            (request.user.is_administrativo or request.user.is_psicologo)
        )
