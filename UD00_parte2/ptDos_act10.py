import os

from pyzbar.pyzbar import decode
from PIL import Image


#obtenemos todos los elementos de la carpeta actual

# os.listdir(".") obtiene todos los elementos
# de la carpeta actual.

elementos = os.listdir(".")


#Recorremos los archivos de la carpeta actual

for elemento in elementos:

    # Comprobamos que el archivo termine en .png.
    if not elemento.lower().endswith(".png"):
        continue

    # Comprobamos que sea realmente un archivo.
    if not os.path.isfile(elemento):
        continue

    #obtenemos el nombre del alumno a partir del nombre del archivo
    # Quitamos ".png" del nombre.
    nombre_alumno = os.path.splitext(elemento)[0]

    #abrimos la imagen
    imagen = Image.open(elemento)

    #leemos los códigos de barras de la imagen
    codigos = decode(imagen)

    #comprobamos si se ha encontrado algún código de barras
    if len(codigos) == 0:

        print(
            f"{nombre_alumno}: "
            "no se ha encontrado ningún código."
        )

        continue

    #si se ha encontrado algún código de barras, los mostramos
    for codigo in codigos:

        # codigo.data contiene los datos
        # almacenados en el código de barras.
        identificador = codigo.data.decode("utf-8")

        print(
            f"{nombre_alumno} -> {identificador}"
        )