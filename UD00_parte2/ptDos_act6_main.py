from ptDos_act6_models import Escola, Professor, Alumne, session

#Craemos una escuela
escuela = Escola(
    nombre="IES Fausti Barberà",
    localidad="Alaquàs",
    responsable="Director de la escuela"
)

#Creamos algunos profesores
profesor1 = Professor(
    nombre="Joan",
    tipo="ciències"
)

profesor2 = Professor(
    nombre="Laura",
    tipo="lletres"
)

#Relacionamos los profesores con la escuela
escuela.profesores.append(profesor1)
escuela.profesores.append(profesor2)

#Creamos algunos alumnos
alumno1 = Alumne(
    nombre="Carlos",
    curso="1º ESO",
    responsable=profesor1
)

alumno2 = Alumne(
    nombre="Ana",
    curso="2º ESO",
    responsable=profesor2
)

#Relacionamos los alumnos con la escuela
escuela.alumnos.append(alumno1)
escuela.alumnos.append(alumno2)


#Guardamos la escuela, los profesores y los alumnos en la base de datos
session.add(escuela)

# commit() confirma los cambios.
session.commit()

print("Datos guardados correctamente.")

#Mostramos Datos
print("\n========== ESCUELAS ==========")

escuelas = session.query(Escola).all()

for escuela in escuelas:
    print(escuela)

    print("\nProfesores:")

    for profesor in escuela.profesores:
        print(" -", profesor)

    print("\nAlumnos:")

    for alumno in escuela.alumnos:
        print(" -", alumno)


#Modificamos un alumno
alumno1.nombre = "Carlos García"
alumno1.curso = "2º ESO"

session.commit()
print("\nAlumno modificado correctamente.")


#Comprobamos la modificación
alumno_modificado = session.query(Alumne).filter_by(
    nombre="Carlos García"
).first()

print("Alumno después de modificar:")
print(alumno_modificado)

#Modificamos un profesor
profesor1.tipo = "mixt"
session.commit()

print("\nProfesor modificado correctamente.")
print(profesor1)


#Eliminamos un alumno
session.delete(alumno2)
session.commit()

print("\nAlumno eliminado correctamente.")


#Mostramos los alumnos actuales después de eliminar uno
print("\n========== ALUMNOS ACTUALES ==========")

alumnos = session.query(Alumne).all()
for alumno in alumnos:
    print(alumno)

#Cerramos la sesión al final del programa
session.close()
print("\nSesión cerrada.")