import sys
import os
try:
    ruta = sys.argv[1]
    extension = sys.argv[2]
except IndexError:
    print("Error, Falta parámetro de extension")   
    sys.exit() 

try:
    lista_de_archivos = os.listdir(ruta)
except FileNotFoundError:
    print("Error, la ruta no existe")
    sys.exit()    

# if not extension.endswith("."):
#     extension = "." + extension
 
archivos_por_extension = []

for archivos in lista_de_archivos:
    if archivos.endswith(extension):
        archivos_por_extension.append("-> "+ archivos) #acá guardo los archivos con sus respectivas extensiones

if len(archivos_por_extension)>0: #si el lenght de los archivos con sus extensiones guardadas es mayor a 0 
#imprimo, caso contrario no hay archivos con esa extension
    print("Archivos con extension ." + extension+"\n")
    for archivo in archivos_por_extension:
        print(archivo)
else:
    print("No hay archivos con esa extension")
    
    
