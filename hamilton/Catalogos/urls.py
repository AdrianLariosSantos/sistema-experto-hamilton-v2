from django.urls import path, include
from rest_framework import routers
from .viewsets import CategoriasViewsets, GenerosViewsets, OpcionesViewsets, PreguntasViewsets, SepoMexViewsets, EdadesViewsets

router = routers.DefaultRouter()  # IMPORTANTE usar DefaultRouter

router.register('catalogo-categorias', CategoriasViewsets, basename='catalogo-categorias')
router.register('catalogo-generos', GenerosViewsets, basename='catalogo-generos')
router.register('catalogo-opciones', OpcionesViewsets, basename='catalogo-opciones')
router.register('catalogo-preguntas', PreguntasViewsets, basename='catalogo-preguntas')
router.register('catalogo-sepomex', SepoMexViewsets, basename='catalogo-sepomex')
router.register('catalogo-edades', EdadesViewsets, basename='catalogo-edades')

urlpatterns = router.urls
