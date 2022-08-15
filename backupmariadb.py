import os, subprocess

ruta_archivo='/home/rsa-key-20211019/MariaDbAsociacion/BackupsUnploaded.txt'
ruta_carpeta='/home/rsa-key-20211019/MariaDbAsociacion/Backups'

def leer_archivo(ruta_a):
    archivo = open(ruta_a)
    BackupsUnploaded= archivo.read()
    temp = list(BackupsUnploaded.split('\n'))
    archivo.close()
    return temp

def leer_carpeta(ruta_c):
    BackupList = list(os.listdir(ruta_c))
    return BackupList

def comparar_conjuntos(c_carpeta,c_archivo ):
    c_carpeta=set(c_carpeta)
    c_archivo=set(c_archivo)
    nuevo =list(c_carpeta.difference(c_archivo))
    return nuevo

def subir_archivo_a_gdrive(regitro_nuevo, ruta_a):
    if len(regitro_nuevo) > 0 :
        bfile = open(ruta_a, 'a')
        for i in regitro_nuevo:
            resultado = subprocess.run(["/home/rsa-key-20211019/MariaDbAsociacion/gdrive", "upload", "-p", "12roKtlktgzmohAhbsy53YeU1HCDqbRix", "/home/rsa-key-20211019/MariaDbAsociacion/Backups/"+i])
            bfile.write("\n"+i)
            print(resultado)
            print(i)
        bfile.close()
    else:
        print('regitro_nuevo vacio')

def eliminar_archivo(ruta, archivo):
    archivo_a_eliminar=archivo.pop(0)
    try:
        os.remove(os.path.join(ruta,archivo_a_eliminar ))
        resultado=True
    except FileNotFoundError as e:
        print(f" Error while search file {e} ")
        resultado=False
    return resultado

def eliminar_registro(lista_archivos, archivo):
    lista_archivos.pop(0)
    lista_temporal= open(archivo, 'w')
    text=''
    for i in reversed(lista_archivos):
        text= i+'\n' + text
    text= text.rstrip()
    lista_temporal.write(text)       
    lista_temporal.close()
    return text

def principal():
    try:
        registro=comparar_conjuntos( leer_carpeta(ruta_carpeta), leer_archivo(ruta_archivo))
        if len(registro) > 0 :
            subir_archivo_a_gdrive(registro, ruta_archivo)
            eliminar_archivo(ruta_carpeta, leer_archivo(ruta_archivo))
            eliminar_registro(leer_archivo(ruta_archivo), ruta_archivo)
        else:
            print('No se genero ningun nuevo archivo de Backup')

        print('Ejecucion Exitosa!')    
    except ValueError:
        print('error en la ejecucion')



#print(type(leer_archivo(ruta_archivo)))
#print(type(leer_carpeta(ruta_carpeta)))
#print(comparar_conjuntos(leer_carpeta(ruta_carpeta), leer_archivo(ruta_archivo)))

principal()