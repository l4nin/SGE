# Name: Alan Souza      --         2DAM
# UD00. Actividad Evaluable 01


#4. ACTIVITAT 01
#Prepara amb un exemple on expliques com fer en Python 3:

#● Clonar una llista.

lista1 = [1, 2, 3, 4]
lista2 = lista1.copy()

#copy() crea una copia de la lista.

print(lista1)
print(lista2)


#○ ¿Quina és la diferència en Python entre “shallow copy” i “deep copy”?

#Shallow copy = copia superficial.
lista2 = lista1.copy()
print(lista2)

#Copia la estructura exterior, pero los objetos que están dentro pueden seguir siendo compartidos.

#Deep copy = copia profunda.

import copy
lista2 = copy.deepcopy(lista1)

#Crea una copia independiente también de los elementos internos.

print(lista2)

#● Afegir un element a una llista.

frutas = ["manzana", "pera"]
frutas.append("plátano")

print(frutas)

#append() añade un elemento al final.

#● Llevar un element a una llista.

frutas = ["manzana", "pera", "plátano"]
frutas.remove("pera")

print(frutas)

#remove() elimina el elemento indicado.


#● Crear una nova llista amb els 4 últims elements d’una llista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

ultimos = numeros[-4:]

print(ultimos)

#-4: significa: Desde los cuatro últimos elementos hasta el final.


#● Convertir les paraules d’una cadena (separades per espai) a una llista.

texto = "Hola me llamo Alan"

palabras = texto.split()

print(palabras)

#split() separa el texto utilizando los espacios.

#● Comentaris amb una línia.

# Se utiliza #: para hacer un comentario 

#● Comentaris multilínia.

"""
Este es un comentario
que ocupa varias líneas.
"""



