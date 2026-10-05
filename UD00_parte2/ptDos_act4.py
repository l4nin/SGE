def contandoMinas(miCampo):
    """
    Recibe una matriz con:
    0  -> casilla sin mina
    -1 -> casilla con mina

    Devuelve otra matriz indicando cuántas minas
    hay alrededor de cada casilla que no tiene mina.
    """
    #Creamos una matriz con las mismas dimensiones que la matriz original
    resultado = []

    for fila in miCampo:
        resultado.append([0] * len(fila))

    #Recorremos todas las filas
    for fila in range(len(miCampo)):

        #Recorremos todas las columnas
        for columna in range(len(miCampo[fila])):

            #Si la casilla contiene una mina, mantenemos el valor -1
            if miCampo[fila][columna] == -1:
                resultado[fila][columna] = -1
                continue

            # Contador de minas cercanas
            minas = 0

            #Comprobamos las 8 posiciones que rodean a la casilla actual
            for cambio_fila in [-1, 0, 1]:
                for cambio_columna in [-1, 0, 1]:

                    #No comprobamos la propia casilla
                    if cambio_fila == 0 and cambio_columna == 0:
                        continue

                    #Calculamos la posición de la casilla vecina
                    nueva_fila = fila + cambio_fila
                    nueva_columna = columna + cambio_columna

                    #Comprobamos que la posición esté dentro de los límites de la matriz
                    if (
                        0 <= nueva_fila < len(miCampo)
                        and 0 <= nueva_columna < len(miCampo[nueva_fila])
                    ):

                        #Si la casilla vecina contiene una mina, aumentamos el contador
                        if miCampo[nueva_fila][nueva_columna] == -1:
                            minas += 1

            #Guardamos el número de minas encontradas
            resultado[fila][columna] = minas

    #Devolvemos la matriz resultante.
    return resultado


#leemos el campo del Buscaminas introducido por el usuario
miCampo = []

print("Introduce el campo del Buscaminas.")
print("Escribe una fila de números separada por espacios.")
print("Utiliza 0 para una casilla vacía y -1 para una mina.")
print("Escribe una línea vacía para terminar.")

while True:

    linea = input()

    #Si el usuario introduce una línea vacía, terminamos la entrada de datos.
    if linea == "":
        break

    #Convertimos los valores introducidos en números enteros.
    fila = list(map(int, linea.split()))

    #Añadimos la fila al campo.
    miCampo.append(fila)

#calculamos el resultado llamando a la función contandoMinas()
resultado = contandoMinas(miCampo)

#Mostramos el resultado al usuario
print("\nResultado:")

for fila in resultado:
    print(*fila)