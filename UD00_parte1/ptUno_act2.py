#ACTIVITAT 02
#En Python 3 els tipus simples passen per valor i els compostos per referència.
#Crea un exemple amb 3 funcions que:

#● Reva 2 números i torne la suma.

def sumar(a, b):
    return a + b


resultado = sumar(5, 3)

print(resultado)

#● Reva una llista i modifique eixa mateixa llista (referència) doblant els valors de tots els
#elements. No ha de retornar res.

def doblar_lista(lista):
    for i in range(len(lista)):
        lista[i] = lista[i] * 2


numeros = [1, 2, 3, 4]

doblar_lista(numeros)

print(numeros)

#● Reva una llista i torne una còpia de la llista mateixa llista (referència) doblant els valors de
#tots els elements. La llista original no hi ha de modificar-se

def doblar_lista_copia(lista):
    copia = lista.copy()

    for i in range(len(copia)):
        copia[i] = copia[i] * 2

    return copia


numeros = [1, 2, 3, 4]

resultado = doblar_lista_copia(numeros)

print("Original:", numeros)
print("Copia:", resultado)