def remove_noise(message):
    """
    Elimina el ruido de un mensaje.

    Args:
        message (str): Mensaje recibido, con posible ruido mezclado.

    Returns:
        str: El mensaje sin los caracteres de ruido (%$&/#·@|º\\ª).

    Example:
        >>> remove_noise("h%e&·%$·llo w&%or&$l·$%d")
        'hello world'
        >>> remove_noise("º¤£ª")
        '¤£'
    """
    # Caracteres que se consideran ruido
    # La barra invertida se escribe doble (\\) porque \ es un carácter especial en Python
    ruido = "%$&/#·@|º\\ª"

    # Cadena donde iremos guardando los caracteres buenos
    resultado = ""

    # Revisamos cada carácter del mensaje
    for c in message:
        # Si no es ruido, lo añadimos al resultado
        if c not in ruido:
            resultado += c

    # Devolvemos el mensaje limpio
    return resultado

# Pruebas con los ejemplos del enunciado
print(remove_noise("h%e&·%$·llo w&%or&$l·$%d"))  # hello world
print(remove_noise(""))                          # (cadena vacía)
print(remove_noise("%$"))                        # (cadena vacía)
print(remove_noise("abcd"))                      # abcd
print(remove_noise("º¤£ª"))                      # ¤£