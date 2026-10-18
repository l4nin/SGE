def repeat_it(n, s):
    """
    Repite una cadena exactamente n veces.

    Args:
        n (int): Número de repeticiones (entero no negativo).
        s (str): Cadena que se quiere repetir.

    Returns:
        str: La cadena s repetida n veces. Si n es 0, devuelve "".

    Example:
        >>> repeat_it(6, "I")
        'IIIIII'
        >>> repeat_it(5, "Hello")
        'HelloHelloHelloHelloHello'
    """
    # El operador * aplicado a una cadena la repite tantas veces como indique el número
    return s * n


# Pruebas
print(repeat_it(6, "I"))      # IIIIII
print(repeat_it(5, "Hello"))  # HelloHelloHelloHelloHello
print(repeat_it(0, "Hi"))     # (cadena vacía)
