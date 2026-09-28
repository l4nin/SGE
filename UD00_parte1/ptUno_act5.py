#ACTIVITAT 05
#Posa un exemple de com passar diversos paràmetres des de consola a un programa Python 3.
#Posa un exemple de com fer “sobrecàrrega de funcions” (funcions que poden rebre diversos
#números de paràmetres), incloent-hi el cas de què el nombre de paràmetres no siga definit

import sys

#Ejemplo de lectura de argumentos desde la consola
def leer_argumentos_consola():
    print("Nombre del script:", sys.argv[0])
    print("Número de argumentos recibidos:", len(sys.argv) - 1)
    print("Lista de argumentos:", sys.argv[1:])


#Ejemplo de "Sobrecarga de funciones"

#Sobrecarga con parámetros por defecto
def calcular_area(base, altura=None):
    if altura is None:
        # Si recibe 1 argumento, asume que es un cuadrado
        return base * base
    # Si recibe 2 argumentos, calcula el área de un rectángulo
    return base * altura


#Sobrecarga con número indefinido de parámetros (*args)
def sumar_varios(*numeros):
    """Suma un número indefinido de parámetros pasados a la función."""
    return sum(numeros)


if __name__ == "__main__":
    print("--- Argumentos de Consola ---")
    leer_argumentos_consola()

    print("\n--- Sobrecarga con parámetros opcionales ---")
    print("Área de cuadrado (lado 4):", calcular_area(4))
    print("Área de rectángulo (base 4, altura 5):", calcular_area(4, 5))

    print("\n--- Sobrecarga indefinida (*args) ---")
    print("Suma de 2 números (5, 10):", sumar_varios(5, 10))
    print("Suma de 5 números (1, 2, 3, 4, 5):", sumar_varios(1, 2, 3, 4, 5))
    print("Suma sin parámetros:", sumar_varios())