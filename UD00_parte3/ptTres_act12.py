def find_short(s):
    """
    Devuelve la longitud de la palabra más corta de una cadena.

    Args:
        s (str): Cadena con palabras separadas por espacios (nunca vacía).

    Returns:
        int: Longitud de la palabra más corta.

    Example:
        >>> find_short("bitcoin take over the world maybe who knows perhaps")
        3
        >>> find_short("turns out random test cases are easier than writing out basic ones")
        3
    """
    # split() separa la cadena en una lista de palabras (por los espacios)
    palabras = s.split()

    # Calculamos la longitud de cada palabra con len()
    longitudes = [len(p) for p in palabras]

    # min() devuelve la longitud más pequeña
    return min(longitudes)


# Pruebas
print(find_short("bitcoin take over the world maybe who knows perhaps"))  # 3
print(find_short("turns out random test cases are easier than writing out basic ones"))  # 3