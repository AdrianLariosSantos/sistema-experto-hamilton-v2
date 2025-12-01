from django.urls import path, include
from rest_framework import routers
from .viewsets import (
    CategoriasViewsets, 
    GenerosViewsets, 
    OpcionesViewsets, 
    PreguntasViewsets, 
    SepoMexViewsets, 
    EdadesViewsets,
    EscolaridadViewsets,
    OcupacionViewsets,
    ParentescoViewsets
)

router = routers.DefaultRouter()

router.register('categorias', CategoriasViewsets, basename='categorias')
router.register('generos', GenerosViewsets, basename='generos')
router.register('opciones', OpcionesViewsets, basename='opciones')
router.register('preguntas', PreguntasViewsets, basename='preguntas')
router.register('sepomex', SepoMexViewsets, basename='sepomex')
router.register('edades', EdadesViewsets, basename='edades')
router.register('escolaridad', EscolaridadViewsets, basename='escolaridad')
router.register('ocupacion', OcupacionViewsets, basename='ocupacion')
router.register('parentesco', ParentescoViewsets, basename='parentesco')

urlpatterns = router.urls
