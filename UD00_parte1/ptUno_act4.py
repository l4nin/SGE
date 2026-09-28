#ACTIVITAT 04
#Explica amb exemples com funcionen els operadors “is”, “not”, “in” en Python 3.

# Operador 'is' (Identidad de memoria)
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a == b (Mismo contenido): {a == b}")  # True
print(f"a is b (Mismo objeto en memoria): {a is b}")  # False
print(f"a is c (Mismo objeto en memoria): {a is c}")  # True

# Operador 'not' (Negación lógica)
es_valido = False
print(f"not es_valido: {not es_valido}")  # True

# Operador 'in' (Pertenencia)
frutas = ["manzana", "platano", "naranja"]
print(f"'platano' in frutas: {'platano' in frutas}")  # True
print(f"'uva' in frutas: {'uva' in frutas}")  # False

# Combinación 'not in' / 'is not'
print(f"'uva' not in frutas: {'uva' not in frutas}")  # True
print(f"a is not b: {a is not b}")  # True