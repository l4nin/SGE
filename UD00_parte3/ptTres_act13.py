def filter_list(l):
    """
    Filtra una lista y devuelve solo los números enteros (quita las cadenas).

    Args:
        l (list): Lista con enteros no negativos y cadenas mezclados.

    Returns:
        list[int]: Nueva lista solo con los enteros, en el mismo orden.

    Example:
        >>> filter_list([1, 2, 'a', 'b'])
        [1, 2]
        >>> filter_list([1, 'a', 'b', 0, 15])
        [1, 0, 15]
        >>> filter_list([1, 2, 'aasf', '1', '123', 123])
        [1, 2, 123]
    """
    # Lista por comprensión: nos quedamos solo con los elementos que son int
    # isinstance(x, int) devuelve True si x es un entero
    return [x for x in l if isinstance(x, int)]


# Pruebas
print(filter_list([1, 2, 'a', 'b']))                # [1, 2]
print(filter_list([1, 'a', 'b', 0, 15]))            # [1, 0, 15]
print(filter_list([1, 2, 'aasf', '1', '123', 123])) # [1, 2, 123]