#ACTIVITAT 03
#Partint d’un context en què volem emmagatzemar un usuari i la seua contrasenya. Fes un exemple
#que explica com es faria:

#● Utilitzant una llista
#● Utilitzant un diccionari.

import hashlib


#Función auxiliar para convertir texto plano a Hash SHA-256
def generar_hash(password: str) -> str:
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


#Datos iniciales (5 usuarios y contraseñas)
datos_raw = [
    ("admin", "1234"),
    ("ALAN", "abcde"),
    ("FRAN", "pass2024"),
    ("AITOR", "qwerty"),
    ("ADRIA", "secret"),
]

#Estructura basada en listas
lista_usuarios = []
for usuario, pwd in datos_raw:
    lista_usuarios.append([usuario, generar_hash(pwd)])


def consultar_lista(user_buscado):
    for u, hash_p in lista_usuarios:
        if u == user_buscado:
            return hash_p
    return "Usuario no encontrado"


#Estructura basada en DICCIONARIOS 
dict_usuarios = {usuario: generar_hash(pwd) for usuario, pwd in datos_raw}


def consultar_diccionario(user_buscado):
    return dict_usuarios.get(user_buscado, "Usuario no encontrado")


print("Consulta 'ALAN':", consultar_lista("ALAN"))
print("Consulta 'no_existe':", consultar_lista("no_existe"))

print("\n--- Consultas en Diccionario ---")
print("Consulta 'admin':", consultar_diccionario("admin"))
print("Consulta 'desconocido':", consultar_diccionario("desconocido"))