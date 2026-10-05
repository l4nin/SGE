#Función que comprueba si un Sudoku es correcto
def esSudokuCorrecto(miArrayBi):

    #Comproba si el Sudoku tiene 9 filas
    if len(miArrayBi) != 9:
        return False

    #Comproba si cada fila tiene 9 números
    for fila in miArrayBi:
        if len(fila) != 9:
            return False
        

    #Recorremos las 9 filas del Sudoku
    for fila in miArrayBi:

        #Comprobamos que no haya números repetidos
        if len(set(fila)) != 9:
            return False

        #Comprobamos que los números estén entre 1 y 9
        for numero in fila:
            if numero < 1 or numero > 9:
                return False


    #Recorremos las 9 columnas.
    for columna in range(9):

        #Creamos una lista con los números de la columna
        numeros_columna = []

        for fila in range(9):
            numeros_columna.append(miArrayBi[fila][columna])

        #Si hay números repetidos, el Sudoku es incorrecto.
        if len(set(numeros_columna)) != 9:
            return False


    
    #Comprobamos los cuadrados 3x3 y recorremos las filas iniciales de cada cuadrado
    for fila_inicio in range(0, 9, 3):

        #Recorremos las columnas iniciales de cada cuadrado
        for columna_inicio in range(0, 9, 3):

            numeros_cuadrado = []

            #Recorremos las 3 filas del cuadrado.
            for fila in range(fila_inicio, fila_inicio + 3):

                #Recorremos las 3 columnas del cuadrado.
                for columna in range(
                    columna_inicio,
                    columna_inicio + 3
                ):
                    numeros_cuadrado.append(
                        miArrayBi[fila][columna]
                    )

            #Comprobamos que no haya números repetidos.
            if len(set(numeros_cuadrado)) != 9:
                return False

    #Si todas las comprobaciones son correctas,
    #devolvemos True.
    return True


#leemos el Sudoku desde un fichero de texto

miArrayBi = []

# Abrimos el fichero Sudoku.in en modo lectura.
with open("Sudoku.in", "r") as archivo:

    # Leemos cada línea del fichero.
    for linea in archivo:

        # Quitamos espacios y saltos de línea.
        linea = linea.strip()

        # Si la línea no está vacía, la procesamos.
        if linea:
            numeros = list(map(int, linea.split()))
            miArrayBi.append(numeros)


print("Sudoku:")

for fila in miArrayBi:
    print(fila)

#comprobamos si el Sudoku es correcto y mostramos el resultado

if esSudokuCorrecto(miArrayBi):
    print("Correcte")
else:
    print("Incorrecte")