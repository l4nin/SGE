#ACTIVITAT 06
#Crea un llistat en el qual cada element d’eixa llista siga una llista amb dos valors: mida i pes.
#Utilitzant https://docs.python.org/3/howto/sorting.html i las “key functions”, fer que aquesta llista
#s’ordene per major altura i en cas d’igualtat, per menor pes.
#SISTEMES DE GESTIÓ EMPRESARIAL UD00 - PÀGINA 4
#SISTEMES DE GESTIÓ EMPRESARIAL UD00. ACTIVITATS AVALUABLES 01
#Explica en comentaris que és realment la “key function”. Pista: en l’ajuda diuen
#“The value of the key parameter should be a function (or other callable) that takes a single
#argument and returns a key to use for sorting purposes. This technique is fast because the key
#function is called exactly once for each input record.”.

#Lista donde cada elemento es [medida/altura, peso]
personas = [
    [180, 75],
    [165, 60],
    [180, 70],  # Empate en altura con el primero, pero menor peso
    [175, 80],
    [190, 85],
    [165, 55],  # Empate en altura con el segundo, pero menor peso
]

"""
EXPLICACIÓN DE LA KEY FUNCTION:
La 'key function' recibe un único argumento (en este caso el elemento 'x' -> [altura, peso])
y devuelve una tupla que Python utiliza para establecer el orden de comparación.

Al devolver (-x[0], x[1]):
- Negamos la altura (-x[0]) para lograr un orden DESCENDENTE (cuanto mayor sea la altura, menor será el valor negativo).
- Dejamos el peso positivo (x[1]) para lograr un orden ASCENDENTE en caso de empate.
"""

personas_ordenadas = sorted(personas, key=lambda x: (-x[0], x[1]))

print("Lista original:")
for p in personas:
    print(f"Altura: {p[0]} cm, Peso: {p[1]} kg")

print("\nLista ordenada (Mayor altura, y a igualdad, menor peso):")
for p in personas_ordenadas:
    print(f"Altura: {p[0]} cm, Peso: {p[1]} kg")