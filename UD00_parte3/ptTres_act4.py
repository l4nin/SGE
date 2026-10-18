def positive_sum(arr):
    """
    Suma todos los números positivos de una lista.

    Args:
        arr (list[int]): Lista de números (positivos, negativos o cero).

    Returns:
        int: Suma de los números positivos. Devuelve 0 si no hay ninguno
        o si la lista está vacía.

    Example:
        >>> positive_sum([1, -4, 7, 12])
        20
        >>> positive_sum([-1, -2, -3])
        0
    """
    # Recorremos la lista y nos quedamos solo con los números mayores que 0
    positivos = [n for n in arr if n > 0]

    # sum() suma todos los elementos; si la lista está vacía devuelve 0
    return sum(positivos)


# Pruebas
print(positive_sum([1, -4, 7, 12]))  # 20  (1 + 7 + 12)
print(positive_sum([-1, -2, -3]))    # 0   (no hay positivos)
print(positive_sum([]))              # 0   (lista vacía)