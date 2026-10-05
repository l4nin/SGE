import sys

#Función para comprobar si un número es palíndromo
def esPalindromo(numero):
    """
    Comprueba si un número es un palíndromo.

    Un palíndromo es un número que se lee igual
    de izquierda a derecha y de derecha a izquierda.

    Ejemplos:
        >>> esPalindromo(5)
        True
        >>> esPalindromo(11)
        True
        >>> esPalindromo(121)
        True
        >>> esPalindromo(123)
        False
    """

    # Convertimos el número a texto.
    texto = str(numero)

    # [::-1] invierte el texto.
    texto_invertido = texto[::-1]

    # Comparamos el texto original con el invertido.
    return texto == texto_invertido


#Función para comprobar si un número es primo
def esPrimo(numero):
    """
    Comprueba si un número es primo.

    Un número primo solamente puede dividirse
    exactamente entre 1 y él mismo.

    Ejemplos:
        >>> esPrimo(2)
        True
        >>> esPrimo(7)
        True
        >>> esPrimo(11)
        True
        >>> esPrimo(10)
        False
        >>> esPrimo(1)
        False
    """

    # Los números menores que 2 no son primos.
    if numero < 2:
        return False

    # Comprobamos si existe algún divisor.
    for divisor in range(2, numero):

        if numero % divisor == 0:
            return False

    # Si no encontramos ningún divisor,
    # el número es primo.
    return True


#Programa principal

# Comprobamos que se hayan indicado los dos archivos.
# sys.argv[0] = nombre del programa
# sys.argv[1] = archivo de entrada
# sys.argv[2] = archivo de salida

if len(sys.argv) != 3:

    print("Uso:")
    print("python3 act7.py archivo_entrada archivo_salida")

    sys.exit(1)


# Guardamos los nombres de los archivos.
archivo_entrada = sys.argv[1]
archivo_salida = sys.argv[2]

# Leemos los números del archivo de entrada
numeros = []

with open(archivo_entrada, "r") as archivo:

    for linea in archivo:

        linea = linea.strip()

        # Ignoramos líneas vacías.
        if linea != "":
            numeros.append(int(linea))


#Contar la cantidad de palíndromos y primos
cantidad_palindromos = 0
cantidad_primos = 0

#Lista para guardar los números que cumplen las dos condiciones
primos_y_palindromos = []


for numero in numeros:

    # Comprobamos si es palíndromo.
    palindromo = esPalindromo(numero)

    # Comprobamos si es primo.
    primo = esPrimo(numero)

    # Si es palíndromo, aumentamos el contador.
    if palindromo:
        cantidad_palindromos += 1

    # Si es primo, aumentamos el contador.
    if primo:
        cantidad_primos += 1

    # Si cumple las dos condiciones,
    # lo guardamos en la lista.
    if palindromo and primo:
        primos_y_palindromos.append(numero)


#Cramos el archivo de salida y escribimos los resultados
with open(archivo_salida, "w") as archivo:

    # Primera línea: cantidad de palíndromos.
    archivo.write(
        f"{cantidad_palindromos}\n"
    )

    # Segunda línea: cantidad de números primos.
    archivo.write(
        f"{cantidad_primos}\n"
    )

    # Después escribimos los números
    # que son primos y palíndromos.
    for numero in primos_y_palindromos:

        archivo.write(
            f"{numero}\n"
        )


print("Proceso terminado correctamente.")
print("Archivo generado:", archivo_salida)