import random


class Car:

    def __init__(self, matricula: int, color: str):
        self.matricula = matricula
        self.color = color
        self.encendido = False

    def imprimir(self):
        print(
            f"Coche -> Matrícula: {self.matricula:04d} | Color: {self.color}"
        )

    #Arrancar
    def arrancar(self):
        self.encendido = True
        print(f"El coche con matrícula {self.matricula} ha arrancado.")

    #Repintar
    def repintar(self, nuevo_color: str):
        self.color = nuevo_color
        print(f"El coche {self.matricula} se ha pintado de {self.color}.")


def main():
    colores_disponibles = ["red", "white", "black", "pink", "blue"]
    coches = []

    try:
        n = int(input("Introduce el número de coches a crear (n): "))
    except ValueError:
        print("Debes introducir un número entero válido.")
        return

    #Creación de n instancias de la clase Car
    for i in range(1, n + 1):
        color_aleatorio = random.choice(colores_disponibles)
        coche = Car(matricula=i, color=color_aleatorio)
        coches.append(coche)

    #Limitar la impresión a un máximo de 10 instancias
    limite = min(n, 10)
    print(f"\n--- Imprimiendo las primeras {limite} instancias ---")
    for i in range(limite):
        coches[i].imprimir()


if __name__ == "__main__":
    main()