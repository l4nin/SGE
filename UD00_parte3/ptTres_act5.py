def double_integer(i):
    """
    Duplica un número entero.

    Args:
        i (int): Número entero a duplicar.

    Returns:
        int: El doble del número recibido.

    Example:
        >>> double_integer(2)
        4
        >>> double_integer(-3)
        -6
    """
    # Multiplicamos el número por 2 y devolvemos el resultado
    return i * 2


# Pruebas
print(double_integer(2))   # 4
print(double_integer(0))   # 0
print(double_integer(-3))  # -6