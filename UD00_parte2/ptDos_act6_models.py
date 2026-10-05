#  MODELOS Y BASE DE DATOS

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    ForeignKey
)

from sqlalchemy.orm import (
    declarative_base,
    relationship,
    sessionmaker
)


#Configuración de la base de datos
#Creamos una base de datos SQLite llamada escuela.db.
#Si el archivo no existe, SQLite lo crea automáticamente.
engine = create_engine("sqlite:///escuela.db")


#Base que utilizaremos para crear las tablas.
Base = declarative_base()

#Clase Escola
class Escola(Base):

    # Nombre de la tabla en SQLite.
    __tablename__ = "escoles"

    # Identificador único de la escuela.
    id = Column(Integer, primary_key=True)

    # Nombre de la escuela.
    nombre = Column(String, nullable=False)

    # Localidad de la escuela.
    localidad = Column(String, nullable=False)

    # Responsable de la escuela.
    responsable = Column(String, nullable=False)

    # Relación con los profesores.
    profesores = relationship(
        "Professor",
        back_populates="escola",
        cascade="all, delete-orphan"
    )

    # Relación con los alumnos.
    alumnos = relationship(
        "Alumne",
        back_populates="escola",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return (
            f"Escola("
            f"id={self.id}, "
            f"nombre='{self.nombre}', "
            f"localidad='{self.localidad}', "
            f"responsable='{self.responsable}')"
        )

#Clase Professor
class Professor(Base):

    __tablename__ = "professors"

    id = Column(Integer, primary_key=True)

    nombre = Column(String, nullable=False)

    tipo = Column(String, nullable=False)

    # Guarda el ID de la escuela a la que pertenece.
    escola_id = Column(
        Integer,
        ForeignKey("escoles.id")
    )

    # Relación con Escola.
    escola = relationship(
        "Escola",
        back_populates="profesores"
    )

    def __repr__(self):
        return (
            f"Professor("
            f"id={self.id}, "
            f"nombre='{self.nombre}', "
            f"tipo='{self.tipo}')"
        )


#Clase Alumne
class Alumne(Base):

    __tablename__ = "alumnes"

    id = Column(Integer, primary_key=True)

    nombre = Column(String, nullable=False)

    curso = Column(String, nullable=False)

    # Escuela a la que pertenece.
    escola_id = Column(
        Integer,
        ForeignKey("escoles.id")
    )

    # Profesor responsable.
    responsable_id = Column(
        Integer,
        ForeignKey("professors.id"),
        nullable=True
    )

    # Relación con Escola.
    escola = relationship(
        "Escola",
        back_populates="alumnos"
    )

    # Relación con Professor.
    responsable = relationship(
        "Professor"
    )

    def __repr__(self):
        if self.responsable:
            responsable = self.responsable.nombre
        else:
            responsable = "Sin responsable"

        return (
            f"Alumne("
            f"id={self.id}, "
            f"nombre='{self.nombre}', "
            f"curso='{self.curso}', "
            f"responsable='{responsable}')"
        )



#Creamos las tablas en la base de datos
Base.metadata.create_all(engine)


#Creamos una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()