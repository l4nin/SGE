def numeroPatrones(text):
    """
    Cuenta cuántas veces aparecen los patrones:
    00, 101, ABC y HO.

    No distingue entre mayúsculas y minúsculas.
    """

    #Convertimos todo el texto a mayúsculas
    #Así podemos buscar los patrones sin distinguir entre mayúsculas y minúsculas
    text = text.upper()

    #Lista con los patrones que queremos buscar.
    patrones = ["00", "101", "ABC", "HO"]

    # Variable donde guardaremos el número total de patrones encontrados
    total = 0

    # Recorremos cada patrón.
    for patron in patrones:

        # Recorremos el texto posición por posición.
        # Usamos range() hasta len(text) - len(patron) + 1
        # para poder comprobar el patrón completo.
        for i in range(len(text) - len(patron) + 1):

            # Comprobamos si el texto que empieza en la posición
            # actual es igual al patrón que estamos buscando
            if text[i:i + len(patron)] == patron:

                # Si encontramos el patrón, aumentamos el contador
                total += 1

    # Devolvemos el número total de patrones encontrados.
    return total


# Pedimos al usuario que introduzca una cadena de texto.
texto = input("Introduce una cadena de texto: ")

# Llamamos a la función numeroPatrones().
resultado = numeroPatrones(texto)

# Mostramos el resultado.
print("Número total de patrones encontrados:", resultado)