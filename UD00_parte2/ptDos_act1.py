from functools import reduce

#Ejemplo sencillo de una función lambda.
#Esta función recibe un número y devuelve su doble.
doble = lambda x: x * 2

print("Ejemplo de lambda:")
print(doble(5))


#Pedimos al usuario una cadena de números separados por espacios.
texto = input("Introduce números separados por espacios: ")


#split() separa la cadena en diferentes elementos.
#map(int, ...) convierte cada elemento de texto en un número entero.
#list() convierte el resultado en una lista.
numeros = list(map(int, texto.split()))

print("Lista de números:")
print(numeros)


# filter() elimina los números menores que 10.
# La lambda devuelve True solamente para números mayores o iguales a 10.
numeros_filtrados = list(
    filter(lambda numero: numero >= 10, numeros)
)

print("Números mayores o iguales que 10:")
print(numeros_filtrados)


# reduce() multiplica todos los elementos de la lista.
# La lambda multiplica el resultado acumulado por el siguiente número.
resultado = reduce(
    lambda acumulado, numero: acumulado * numero,
    numeros_filtrados
)

print("Resultado de la multiplicación:")
print(resultado)