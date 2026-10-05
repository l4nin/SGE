#CLASES DE UNA ESCUELA

class Professor:
    """
    Representa un profesor de la escuela

    Cada profesor tiene:
    - nombre
    - tipo: ciències, lletres o mixt
    - escuela a la que pertenece
    """

    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.escola = None

    def __str__(self):
        return f"Profesor: {self.nombre} | Tipo: {self.tipo}"


class Alumne:
    """
    Representa un alumno.

    Cada alumno tiene:
    - nombre
    - curso
    - profesor responsable
    - escuela a la que pertenece
    """

    def __init__(self, nombre, curso, responsable=None):
        self.nombre = nombre
        self.curso = curso
        self.responsable = responsable
        self.escola = None

    def __str__(self):
        if self.responsable is not None:
            nombre_responsable = self.responsable.nombre
        else:
            nombre_responsable = "Sin responsable"

        return (
            f"Alumno: {self.nombre} | "
            f"Curso: {self.curso} | "
            f"Responsable: {nombre_responsable}"
        )


class Escola:
    """
    Representa una escuela.

    Una escuela puede tener:
    - nombre
    - localidad
    - responsable
    - profesores
    - alumnos
    """

    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable

        #Lista donde guardaremos los profesores.
        self.profesores = []

        #Lista donde guardaremos los alumnos.
        self.alumnos = []

 
    #Metodos para profesores
    def agregar_profesor(self, profesor):
        """
        Añade un profesor a la escuela.
        Un profesor no puede pertenecer a dos escuelas.
        """

        if profesor in self.profesores:
            print("El profesor ya está en esta escuela.")
            return

        if profesor.escola is not None:
            print("El profesor ya pertenece a otra escuela.")
            return

        self.profesores.append(profesor)
        profesor.escola = self

        print(f"Profesor {profesor.nombre} añadido correctamente.")

    def eliminar_profesor(self, profesor):
        """
        Elimina un profesor de la escuela.
        """

        if profesor not in self.profesores:
            print("El profesor no está en esta escuela.")
            return

        self.profesores.remove(profesor)
        profesor.escola = None

        # Si algún alumno tenía a este profesor
        # como responsable, quitamos el responsable.
        for alumno in self.alumnos:
            if alumno.responsable == profesor:
                alumno.responsable = None

        print(f"Profesor {profesor.nombre} eliminado correctamente.")

    def modificar_profesor(self, profesor, nuevo_nombre, nuevo_tipo):
        """
        Modifica los datos de un profesor.
        """

        if profesor not in self.profesores:
            print("El profesor no está en esta escuela.")
            return

        profesor.nombre = nuevo_nombre
        profesor.tipo = nuevo_tipo

        print("Profesor modificado correctamente.")


    #Metodos para alumnos
    def agregar_alumno(self, alumno):
        """
        Añade un alumno a la escuela.
        Un alumno no puede pertenecer a dos escuelas.
        """

        if alumno in self.alumnos:
            print("El alumno ya está en esta escuela.")
            return

        if alumno.escola is not None:
            print("El alumno ya pertenece a otra escuela.")
            return

        # Si tiene profesor responsable,
        # comprobamos que pertenezca a esta escuela.
        if alumno.responsable is not None:
            if alumno.responsable not in self.profesores:
                print(
                    "El profesor responsable debe pertenecer "
                    "a esta escuela."
                )
                return

        self.alumnos.append(alumno)
        alumno.escola = self

        print(f"Alumno {alumno.nombre} añadido correctamente.")

    def eliminar_alumno(self, alumno):
        """
        Elimina un alumno de la escuela.
        """

        if alumno not in self.alumnos:
            print("El alumno no está en esta escuela.")
            return

        self.alumnos.remove(alumno)
        alumno.escola = None

        print(f"Alumno {alumno.nombre} eliminado correctamente.")

    def modificar_alumno(
        self,
        alumno,
        nuevo_nombre,
        nuevo_curso,
        nuevo_responsable
    ):
        """
        Modifica los datos de un alumno.
        """

        if alumno not in self.alumnos:
            print("El alumno no está en esta escuela.")
            return

        # El responsable debe ser un profesor
        # de esta misma escuela.
        if nuevo_responsable is not None:
            if nuevo_responsable not in self.profesores:
                print(
                    "El nuevo responsable debe ser "
                    "un profesor de esta escuela."
                )
                return

        alumno.nombre = nuevo_nombre
        alumno.curso = nuevo_curso
        alumno.responsable = nuevo_responsable

        print("Alumno modificado correctamente.")


    #Mostrar información 
    def mostrar_profesores(self):
        """
        Muestra todos los profesores de la escuela.
        """

        print("\n--- PROFESORES ---")

        if len(self.profesores) == 0:
            print("No hay profesores.")
            return

        for profesor in self.profesores:
            print(profesor)

    def mostrar_alumnos(self):
        """
        Muestra todos los alumnos de la escuela.
        """

        print("\n--- ALUMNOS ---")

        if len(self.alumnos) == 0:
            print("No hay alumnos.")
            return

        for alumno in self.alumnos:
            print(alumno)

    def mostrar_escuela(self):
        """
        Muestra toda la información de la escuela.
        """

        print("\n================================")
        print("INFORMACIÓN DE LA ESCUELA")
        print("================================")

        print("Nombre:", self.nombre)
        print("Localidad:", self.localidad)
        print("Responsable:", self.responsable)

        self.mostrar_profesores()
        self.mostrar_alumnos()