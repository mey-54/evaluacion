class Persona:
    def __init__(self, matricula, dni, nombreApellido, direccion):
        self.matricula = matricula
        self.dni = dni
        self.nombreApellido = nombreApellido
        self.direccion = direccion

    def mostrar_datos(self):
        return (f"Matricula: {self.matricula}, DNI: {self.dni}, "
                f"Nombre y Apellido: {self.nombreApellido}, Direccion: {self.direccion}")

class Estudiante(Persona):
    def __init__(self, matricula, dni, nombreApellido, direccion, anioCurso, materias):
        super().__init__(matricula, dni, nombreApellido, direccion)
        self.anioCurso = anioCurso
        self.materias = materias

    def mostrar_datos(self):
        datos_personales = super().mostrar_datos()
        return (f"{datos_personales}, Año de Curso: {self.anioCurso}, Materias: {', '.join(self.materias)}")

class Docente(Persona):
    def __init__(self, matricula, dni, nombreApellido, direccion, cursosAcargo):
        super().__init__(matricula, dni, nombreApellido, direccion)
        self.cursosAcargo = cursosAcargo

    def mostrar_datos(self):
        datos_personales = super().mostrar_datos()
        return (f"{datos_personales}, Cursos a Cargo: {', '.join(self.cursosAcargo)}")

# Crear objetos para cada clase

# Tres estudiantes
estudiante1 = Estudiante(
    matricula="E001",
    dni="12345678A",
    nombreApellido="Juan Pérez",
    direccion="Calle Falsa 123",
    anioCurso=2,
    materias=["Matemáticas", "Ciencias"]
)

estudiante2 = Estudiante(
    matricula="E002",
    dni="23456789B",
    nombreApellido="Ana Gómez",
    direccion="Avenida Siempre Viva 742",
    anioCurso=1,
    materias=["Historia", "Lengua"]
)

estudiante3 = Estudiante(
    matricula="E003",
    dni="34567890C",
    nombreApellido="Luis Fernández",
    direccion="Calle Mayor 45",
    anioCurso=3,
    materias=["Geografía", "Física"]
)

# Tres docentes
docente1 = Docente(
    matricula="D001",
    dni="45678901D",
    nombreApellido="María López",
    direccion="Plaza del Sol 12",
    cursosAcargo=["Matemáticas", "Ciencias"]
)

docente2 = Docente(
    matricula="D002",
    dni="56789012E",
    nombreApellido="Carlos Martínez",
    direccion="Calle del Prado 34",
    cursosAcargo=["Historia", "Lengua"]
)

docente3 = Docente(
    matricula="D003",
    dni="67890123F",
    nombreApellido="Laura Rodríguez",
    direccion="Calle del Valle 56",
    cursosAcargo=["Geografía", "Física"]
)

# Mostrar datos de estudiantes
print("Datos de Estudiantes:")
print(estudiante1.mostrar_datos())
print(estudiante2.mostrar_datos())
print(estudiante3.mostrar_datos())

# Mostrar datos de docentes
print("\nDatos de Docentes:")
print(docente1.mostrar_datos())
print(docente2.mostrar_datos())
print(docente3.mostrar_datos())
