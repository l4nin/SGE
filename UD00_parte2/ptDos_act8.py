import os
import shutil
import sys

#Función para organizar archivos según su extensión
def organizar_archivos(extensiones):
    """
    Organiza los archivos de la carpeta actual
    según su extensión.

    Por ejemplo:

        png -> carpeta png
        mp4 -> carpeta mp4
        doc -> carpeta doc
    """

    # Obtenemos todos los elementos de la carpeta actual.
    elementos = os.listdir(".")

    # Recorremos las extensiones indicadas.
    for extension in extensiones:

        # Quitamos un posible punto.
        # Así funcionan tanto "png" como ".png".
        extension = extension.lstrip(".")

        # Creamos el nombre de la carpeta.
        carpeta = extension

        # Si la carpeta no existe, la creamos.
        if not os.path.exists(carpeta):
            os.mkdir(carpeta)

        # Recorremos todos los elementos.
        for elemento in elementos:

            # Creamos la ruta completa del elemento.
            ruta = os.path.join(".", elemento)

            # Solo queremos trabajar con archivos.
            if not os.path.isfile(ruta):
                continue

            # Obtenemos la extensión del archivo.
            extension_archivo = os.path.splitext(
                elemento
            )[1].lower()

            # Añadimos un punto para comparar.
            extension_buscada = "." + extension.lower()

            # Si coincide la extensión...
            if extension_archivo == extension_buscada:

                # Creamos la ruta de destino.
                destino = os.path.join(
                    carpeta,
                    elemento
                )

                # Movemos el archivo.
                shutil.move(
                    ruta,
                    destino
                )

                print(
                    f"Movido: {elemento} -> {carpeta}/"
                )


# Programa principal
# Comprobamos que se hayan introducido extensiones.
if len(sys.argv) < 2:

    print("Uso:")
    print(
        "python3 organizar.py png mp4 doc"
    )

    sys.exit(1)


# Los argumentos desde la posición 1 son
# las extensiones que queremos organizar.
extensiones = sys.argv[1:]


# Ejecutamos la función.
organizar_archivos(extensiones)


print("\nOrganización terminada.")