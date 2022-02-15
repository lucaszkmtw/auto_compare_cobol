from django.urls import path
from Municipios.views import guardar_lineas, municipio, parseCobol



urlpatterns = [
    path('', municipio, name="municipio" ),
    path('parse_cobol/' , parseCobol, name="parseCobol" ),
    path('guardar_lineas/' , guardar_lineas, name="guardar_lineas" ),
    


]
