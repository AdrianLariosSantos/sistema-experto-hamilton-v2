from django.urls import path, include
from rest_framework import routers
from .viewsets import AuthViewSet, UsuarioViewSet, RolViewSet

router = routers.DefaultRouter()

router.register('auth', AuthViewSet, basename='auth')
router.register('usuarios', UsuarioViewSet, basename='usuarios')
router.register('roles', RolViewSet, basename='roles')

urlpatterns = router.urls
