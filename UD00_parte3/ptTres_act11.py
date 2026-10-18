def sum_two_smallest_numbers(numbers):
    """
    Suma los dos números más pequeños de una lista.

    Args:
        numbers (list[int]): Lista de al menos 4 enteros positivos.

    Returns:
        int: La suma de los dos números más bajos de la lista.

    Example:
        >>> sum_two_smallest_numbers([19, 5, 42, 2, 77])
        7
        >>> sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453])
        3453455
    """
    # sorted() devuelve una copia de la lista ordenada de menor a mayor
    ordenados = sorted(numbers)

    # Los dos primeros son los más pequeños: los sumamos
    return ordenados[0] + ordenados[1]


# Pruebas
print(sum_two_smallest_numbers([19, 5, 42, 2, 77]))                 # 7   (2 + 5)
print(sum_two_smallest_numbers([10, 343445353, 3453445, 3453545353453]))  # 3453455 (10 + 3453445)