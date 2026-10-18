def make_upper_case(s):
    """
    Convierte una cadena de texto a mayúsculas.

    Args:
        s (str): Cadena de texto a convertir.

    Returns:
        str: La misma cadena con todas las letras en mayúsculas.

    Example:
        >>> make_upper_case("hello")
        'HELLO'
        >>> make_upper_case("Hola Mundo 123")
        'HOLA MUNDO 123'
    """
    # El método upper() devuelve una copia de la cadena en mayúsculas
    # Los números y símbolos no cambian
    return s.upper()


# Pruebas
print(make_upper_case("hello"))           # HELLO
print(make_upper_case("Hola Mundo 123"))  # HOLA MUNDO 123
print(make_upper_case(""))                # (cadena vacía)