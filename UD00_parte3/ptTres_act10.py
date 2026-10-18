def square_sum(numbers):
    """
    Eleva al cuadrado cada número de la lista y suma los resultados.

    Args:
        numbers (list[int]): Lista de números.

    Returns:
        int: La suma de los cuadrados de todos los números.
        Si la lista está vacía, devuelve 0.

    Example:
        >>> square_sum([1, 2, 2])
        9
        >>> square_sum([0, 3, 4, 5])
        50
    """
    # Expresión generadora: elevamos cada número al cuadrado con ** 2
    # sum() suma todos esos cuadrados
    return sum(n ** 2 for n in numbers)


# Pruebas
print(square_sum([1, 2, 2]))     # 9   (1 + 4 + 4)
print(square_sum([0, 3, 4, 5]))  # 50  (0 + 9 + 16 + 25)
print(square_sum([]))            # 0   (lista vacía)