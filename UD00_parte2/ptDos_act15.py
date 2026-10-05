import time
import pyperclip


def cargar_palabras(nombre_archivo):
    """
    Lee las palabras prohibidas desde un archivo.

    Cada palabra debe estar en una línea diferente.
    """

    palabras = []

    with open(
        nombre_archivo,
        "r",
        encoding="utf-8"
    ) as archivo:

        for linea in archivo:

            palabra = linea.strip()

            # Ignoramos líneas vacías.
            if palabra != "":
                palabras.append(palabra)

    return palabras

#Filtramos las palabras prohibidas del texto
def filtrar_texto(texto, palabras):
    """
    Busca las palabras prohibidas dentro del texto.

    La comparación no distingue entre mayúsculas
    y minúsculas.

    Los caracteres de cada palabra encontrada
    se sustituyen por '*'.
    """

    texto_filtrado = texto

    # Recorremos todas las palabras prohibidas.
    for palabra in palabras:

        # Si la palabra está vacía, la ignoramos.
        if palabra == "":
            continue

        # Texto en minúsculas para comparar.
        texto_minusculas = texto_filtrado.lower()

        # Palabra en minúsculas.
        palabra_minuscula = palabra.lower()

        # Posición inicial de búsqueda.
        posicion = 0

        while True:

            # Buscamos la palabra.
            posicion = texto_minusculas.find(
                palabra_minuscula,
                posicion
            )

            # Si no aparece más veces,
            # terminamos este bucle.
            if posicion == -1:
                break

            # Creamos una cadena de asteriscos
            # con la misma longitud que la palabra.
            reemplazo = "*" * len(palabra)

            # Sustituimos la palabra.
            texto_filtrado = (
                texto_filtrado[:posicion]
                + reemplazo
                + texto_filtrado[
                    posicion + len(palabra):
                ]
            )

            # Actualizamos la versión en minúsculas
            # después de la sustitución.
            texto_minusculas = (
                texto_filtrado.lower()
            )

            # Avanzamos después de la palabra.
            posicion += len(reemplazo)

    return texto_filtrado


# =========================================================
# CARGAR LAS PALABRAS
# =========================================================

palabras_prohibidas = cargar_palabras(
    "palabras.txt"
)


print("Filtro del portapapeles iniciado.")
print("Pulsa Ctrl+C para terminar.")


# =========================================================
# VIGILAR EL PORTAPAPELES
# =========================================================

ultimo_texto = pyperclip.paste()


while True:

    try:

        # Leemos el contenido actual.
        texto_actual = pyperclip.paste()


        # Comprobamos si ha cambiado.
        if texto_actual != ultimo_texto:

            # Guardamos el nuevo texto.
            ultimo_texto = texto_actual

            # Filtramos el texto.
            texto_filtrado = filtrar_texto(
                texto_actual,
                palabras_prohibidas
            )


            # Si el texto ha cambiado,
            # lo copiamos de nuevo al portapapeles.
            if texto_filtrado != texto_actual:

                pyperclip.copy(
                    texto_filtrado
                )

                # Actualizamos la variable para evitar
                # procesar otra vez el mismo texto.
                ultimo_texto = texto_filtrado

                print(
                    "Texto filtrado:"
                )

                print(
                    texto_filtrado
                )


        # Esperamos un poco antes de volver a comprobar.
        time.sleep(0.5)


    except KeyboardInterrupt:

        print(
            "\nPrograma terminado."
        )

        break