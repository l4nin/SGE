def shift_left(a, b):
    """
    Calcula el mínimo de movimientos para igualar dos cadenas,
    borrando en cada movimiento el primer carácter de una de ellas.

    Args:
        a (str): Primera cadena (letras minúsculas).
        b (str): Segunda cadena (letras minúsculas).

    Returns:
        int: Número mínimo de movimientos para que ambas cadenas sean iguales.

    Example:
        >>> shift_left("test", "west")
        2
        >>> shift_left("abc", "xyz")
        6
        >>> shift_left("hello", "hello")
        0
    """
    # Como solo borramos por la izquierda, lo único que se conserva
    # es el final de cada cadena. Buscamos el sufijo común más largo.
    comunes = 0

    # Comparamos las dos cadenas empezando por el último carácter
    # min(len(a), len(b)) evita salirnos de la cadena más corta
    for i in range(1, min(len(a), len(b)) + 1):
        # a[-i] y b[-i] son los caracteres en la misma posición contando desde el final
        if a[-i] == b[-i]:
            comunes += 1
        else:
            # En cuanto hay una diferencia, paramos
            break

    # Lo que no es común hay que borrarlo en las dos cadenas
    # Total de caracteres - los que se quedan en cada cadena (comunes * 2)
    return len(a) + len(b) - 2 * comunes


# Pruebas
print(shift_left("test", "west"))    # 2  (queda "est")
print(shift_left("abc", "xyz"))      # 6  (quedan dos cadenas vacías)
print(shift_left("hello", "hello"))  # 0  (ya son iguales)