from django.urls import path
from Municipios.views import municipio, parseCobol



urlpatterns = [
    path('', municipio, name="municipio" ),
    path('parse_cobol/' , parseCobol, name="parseCobol" )



]
