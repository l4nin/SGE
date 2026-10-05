# Importamos las clases que están en ptDos_act5_classes.py
from ptDos_act5_classes import Escola, Professor, Alumne

#creamos una escuela
escola = Escola(
    "IES Faustí Barberá",
    "València",
    "Pilar"
)

#creamos algunos profesores
profesor1 = Professor(
    "Oscar",
    "Raul"
    
)

profesor2 = Professor(
    "Pilar",
    "Borja"
)

profesor3 = Professor(
    "Paco",
    "Henrique"
)

#agregamos los profesores a la escuela
escola.agregar_profesor(profesor1)
escola.agregar_profesor(profesor2)
escola.agregar_profesor(profesor3)


#creamos algunos alumnos
alumno1 = Alumne(
    "Alan",
    "2º DAM",
    profesor1
)

alumno2 = Alumne(
    "Fran",
    "2º DAM",
    profesor2
)

alumno3 = Alumne(
    "Aitor",
    "2º DAM",
    profesor3
)

#agregamos los alumnos a la escuela
escola.agregar_alumno(alumno1)
escola.agregar_alumno(alumno2)
escola.agregar_alumno(alumno3)

#Mostramos la información de la escuela
escola.mostrar_escuela()

#modificamos un profesor
print("\n--- MODIFICANDO PROFESOR ---")

escola.modificar_profesor(
    profesor1,
    "Juan",
    "mixt"
)

#Modificamos un alumno
print("\n--- MODIFICANDO ALUMNO ---")

escola.modificar_alumno(
    alumno1,
    "ADRIA",
    "2º DAM",
    profesor1
)

#mostramos los cambios realizados
print("\n--- MOSTRANDO ESCUELA DESPUÉS DE MODIFICAR ---")
escola.mostrar_escuela()

#eleminamos un alumno
print("\n--- ELIMINANDO ALUMNO ---")

escola.eliminar_alumno(alumno3)


#eliminamos un profesor
print("\n--- ELIMINANDO PROFESOR ---")

escola.eliminar_profesor(profesor2)

#resultado final después de eliminar un alumno y un profesor
print("\n--- RESULTADO FINAL ---")
escola.mostrar_escuela()