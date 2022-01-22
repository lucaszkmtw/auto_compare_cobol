from django.conf import settings
import os


FILE_DIRS = settings.MEDIA_ROOT

mun= '/municipio/'
edit= '/municipio_edit/'
def lecturaArchivo(archivo):
    lista= []  

    
    file1 = open( FILE_DIRS + mun + f'{archivo}.txt', 'r')
    
    print('dividiendo hiscar en cachos')
    for file in file1:
        linea = file.strip()
        # filtrando los de 2021
        lista.append(linea)       
    
    return lista



def editable(lista):
    outFile = open(FILE_DIRS + edit  + "municipio_edit.txt", "w")
    outFile.writelines(lista)
    outFile.close() 
    

def cant_municipios():
    FILE_DIRS = settings.MEDIA_ROOT + mun
    HISCAR_FILES = [dir[0:8] for dir in os.listdir(FILE_DIRS)] if os.path.exists(FILE_DIRS) else []



    return HISCAR_FILES