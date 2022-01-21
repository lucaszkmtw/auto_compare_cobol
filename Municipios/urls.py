from django.urls import path
from Municipios.views import municipio, parseCobol



urlpatterns = [
    path('inicio/', municipio, name="municipio" ),
    path('parse_cobol/' , parseCobol, name="parseCobol" )



]
