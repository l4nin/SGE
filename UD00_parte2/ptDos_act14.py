def es_segura(tablero, fila, columna):
    """
    Comprueba si podemos colocar una reina en
    la posición indicada.

    tablero:
        Lista donde cada posición representa
        la columna donde está colocada la reina
        de esa fila.

    fila:
        Fila donde queremos colocar la reina.

    columna:
        Columna donde queremos colocar la reina.
    """

    # Comprobamos todas las filas anteriores.
    for fila_anterior in range(fila):

        columna_anterior = tablero[fila_anterior]

        if columna_anterior == columna:
            return False


        # La diferencia entre filas y columnas
        # debe ser diferente para evitar diagonales.
        if abs(
            columna_anterior - columna
        ) == abs(
            fila_anterior - fila
        ):
            return False

    # Si no hay ningún conflicto,
    # la posición es segura.
    return True


#Backtracking para colocar las reinas

def colocar_reinas(tablero, fila, n):
    """
    Intenta colocar las reinas restantes.

    Devuelve el número total de soluciones.
    """

    # Si hemos llegado a la última fila,
    # significa que hemos colocado todas las reinas.
    if fila == n:
        return 1

    soluciones = 0

    # Probamos todas las columnas de esta fila.
    for columna in range(n):

        # Comprobamos si la posición es válida.
        if es_segura(
            tablero,
            fila,
            columna
        ):

            # Colocamos la reina.
            tablero[fila] = columna

            # Intentamos colocar la siguiente reina.
            soluciones += colocar_reinas(
                tablero,
                fila + 1,
                n
            )

            # Quitamos la reina para probar
            # otra posibilidad.
            tablero[fila] = -1

    return soluciones

#Función principal para resolver el problema de las N reinas
def resolver_n_reinas(n):
    """
    Calcula el número de soluciones para un tablero
    de tamaño n x n.
    """

    # -1 significa que todavía no hay una reina
    # colocada en esa fila.
    tablero = [-1] * n

    return colocar_reinas(
        tablero,
        0,
        n
    )


#Pedimos al usuario que introduzca un número entre 4 y 10
while True:

    try:

        n = int(
            input(
                "Introduce N (entre 4 y 10): "
            )
        )

        if 4 <= n <= 10:
            break

        print(
            "N debe estar entre 4 y 10."
        )

    except ValueError:

        print(
            "Debes introducir un número entero."
        )


#Calculamos el número de soluciones para el problema de las N reinas
soluciones = resolver_n_reinas(n)

#Mostramos el resultado al usuario
print(
    f"Para N = {n} hay "
    f"{soluciones} soluciones."
)