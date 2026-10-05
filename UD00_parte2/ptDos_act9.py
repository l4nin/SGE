import csv
import sys

import barcode
from barcode.writer import ImageWriter


#Comprobamos que se haya indicado el archivo CSV

#El programa necesita el nombre del archivo CSV.
#Ejemplo: alumnos.csv

if len(sys.argv) != 2:

    print("Uso:")
    print("python3 ptDos_act9.py alumnos.csv")

    sys.exit(1)


#Guardamos el nombre del archivo CSV.
archivo_csv = sys.argv[1]

#leemos el archivo CSV y generamos los códigos de barras EAN-13
with open(
    archivo_csv,
    "r",
    encoding="utf-8"
) as archivo:

    # csv.reader permite leer el CSV
    # separando cada línea por comas.
    lector = csv.reader(archivo)

    # Recorremos todas las líneas.
    for fila in lector:

        # Comprobamos que haya exactamente
        # dos datos: nombre e ID.
        if len(fila) != 2:

            print(
                "Línea incorrecta:",
                fila
            )

            continue

        #Primer dato: nombre del alumno.
        nombre = fila[0].strip()

        #Segundo dato: ID del alumno.
        identificador = fila[1].strip()


        #Comprobamos que el ID sea correcto
        # EAN-13 necesita exactamente 13 números
        if len(identificador) != 13:

            print(
                f"ID incorrecto para {nombre}: "
                f"debe tener 13 dígitos."
            )

            continue

        #Comprobamos que todos los caracteres sean números
        if not identificador.isdigit():

            print(
                f"ID incorrecto para {nombre}: "
                f"solo puede contener números."
            )

            continue

        # Crear un objeto EAN-13 
        # Creamos un objeto EAN-13.
        codigo = barcode.get(
            "ean13",
            identificador,
            writer=ImageWriter()
        )



        #Creamos el archivo de imagen con el código de barras
        
        # El nombre del archivo será el nombre del alumno.
        # Si nombre = "Carlos":
        # se creará:
        # Carlos.png

        codigo.save(nombre)

        print(
            f"Código generado para {nombre}: "
            f"{nombre}.png"
        )


print("\nProceso terminado.")