def bool_to_word(boolean):
    """
    Convierte un valor booleano en la palabra "Yes" o "No".

    Args:
        boolean (bool): Valor a convertir (True o False).

    Returns:
        str: "Yes" si el valor es True, "No" si es False.

    Example:
        >>> bool_to_word(True)
        'Yes'
        >>> bool_to_word(False)
        'No'
    """
    #Si boolean es True devuelve "Yes", si no, "No"
    return "Yes" if boolean else "No"

# Pruebas
print(bool_to_word(True))   # Yes
print(bool_to_word(False))  # No