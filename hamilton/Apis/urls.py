from django.urls import path, include


urlpatterns = [
    path('catalogos/', include('Catalogos.urls')),
    path('entrenamiento/', include('Entrenamiento.urls')),

]