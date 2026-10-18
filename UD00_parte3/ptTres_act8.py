def century(year):
    """
    Calcula el siglo al que pertenece un año.

    Args:
        year (int): Año del que se quiere saber el siglo (mayor que 0).

    Returns:
        int: Número del siglo. El siglo 1 va del año 1 al 100,
        el siglo 2 del 101 al 200, etc.

    Example:
        >>> century(1705)
        18
        >>> century(1900)
        19
        >>> century(2000)
        20
    """
    # Restamos 1 al año para que el año 100 siga en el siglo 1
    # (sin esto, 100 // 100 daría 1 y pasaría al siglo 2 con el +1)
    # Con // (división entera) nos quedamos solo con la parte entera
    # Sumamos 1 porque los siglos empiezan a contarse desde 1, no desde 0
    return (year - 1) // 100 + 1


# Pruebas con los ejemplos del enunciado
print(century(1705))  # 18
print(century(1900))  # 19
print(century(1601))  # 17
print(century(2000))  # 20
print(century(2742))  # 28

