from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.
from .models import Linea, Municipio
from Municipios import archivos

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def municipio(request):

    
    archivo = archivos.cant_municipios()
    nuevo = None
    if request.method == "POST":
        nuevo = request.POST.get('opcion')

    # muni = Municipio(
    #     nombre = 'BAHIA BLANCA',
    #     codigo = 'GEHIM007',
    # )
    # muni.save()
    
    # gehim = Municipio.objects.get(codigo='GEHIM007')
    # for linea in lineas:
    #     nueva_linea= Linea(
    #         texto = linea,
    #         mun =  gehim
    #     )
    #     nueva_linea.save()

 #   archivos.editable(lineas)
    context = {
        'nuevo':nuevo,
        'archivo':archivo,
    }
    return render(request, 'municipio.html', context )




def parseCobol(request):

    archivo = request.GET['archivo']
    lineas = archivos.lecturaArchivo(archivo) 

    context = {

        'lineas':lineas,
    }

    return JsonResponse(context, safe=True)




def guardar_lineas(request):
    context = {'asd':'asd'}
    return render(request, 'modal.html', context)


def guardar(request):
    data= {}
    if is_ajax(request=request):
        linea = request.POST.get('linea')
        
    return JsonResponse(data)
