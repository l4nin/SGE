def summation(num):
    """
    Suma todos los números enteros desde 1 hasta num (ambos incluidos).

    Args:
        num (int): Número entero positivo mayor que 0.

    Returns:
        int: La suma de 1 + 2 + 3 + ... + num.

    Example:
        >>> summation(2)
        3
        >>> summation(8)
        36
    """
    # Fórmula de Gauss: la suma de 1 a n es n * (n + 1) / 2
    # Usamos // (división entera) para que el resultado sea un int y no un float
    return num * (num + 1) // 2


# Pruebas con los ejemplos del enunciado
print(summation(2))  # 3   (1 + 2)
print(summation(8))  # 36  (1 + 2 + ... + 8)