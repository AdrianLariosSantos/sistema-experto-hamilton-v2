from django.urls import path, include
from rest_framework import routers
from Entrenamiento.viewsets import EntrenamientoViewsets

router = routers.DefaultRouter()  # IMPORTANTE usar DefaultRouter

router.register('conocimiento-entrenamiento', EntrenamientoViewsets, basename='conocimiento-entrenamiento')


urlpatterns = router.urls