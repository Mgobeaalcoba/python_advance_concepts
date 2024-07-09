from typing import Type, Callable

class Persona:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad
        self.get_nombre: Callable[[], str] = lambda: self._nombre
        self.set_nombre: Callable[[str], None] = lambda nombre: setattr(self, '_nombre', nombre)
        self.get_edad: Callable[[], int] = lambda: self._edad
        self.set_edad: Callable[[int], None] = lambda edad: setattr(self, '_edad', edad)
        self.presentarse: Callable[[], str] = lambda: f"Hola, mi nombre es {self._nombre} y tengo {self._edad} años."

    def __str__(self):
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}"

class Materia:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self.get_nombre: Callable[[], str] = lambda: self._nombre
        self.set_nombre: Callable[[str], None] = lambda nombre: setattr(self, '_nombre', nombre)

    def __str__(self):
        return f"Materia: {self.get_nombre()}"

class Salario:
    def __init__(self, cantidad: float):
        self._cantidad = cantidad
        self.get_cantidad: Callable[[], float] = lambda: self._cantidad
        self.set_cantidad: Callable[[float], None] = lambda cantidad: setattr(self, '_cantidad', cantidad)
        self.incrementar: Callable[[float], 'Salario'] = lambda porcentaje: Salario(self._cantidad * (1 + porcentaje / 100))

    def __str__(self):
        return f"Salario: {self.get_cantidad()}"

class Docente(Persona):
    def __init__(self, nombre: str, edad: int, materia: Type[Materia], salario: Type[Salario]):
        super().__init__(nombre, edad)
        self._materia = materia
        self._salario = salario
        self.get_materia: Callable[[], Materia] = lambda: self._materia
        self.set_materia: Callable[[Materia], None] = lambda materia: setattr(self, '_materia', materia)
        self.get_salario: Callable[[], Salario] = lambda: self._salario
        self.set_salario: Callable[[Salario], None] = lambda salario: setattr(self, '_salario', salario)
        self.enseñar: Callable[[], str] = lambda: f"Enseñando la materia {self._materia.get_nombre()}."
        self.ver_salario: Callable[[], str] = lambda: f"El salario es {self._salario.get_cantidad()}."

    def __str__(self):
        return f"{super().__str__()}, Materia: {self.get_materia().get_nombre()}, Salario: {self.get_salario().get_cantidad()}"

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, materia: Type[Materia]):
        super().__init__(nombre, edad)
        self._materia = materia
        self.get_materia: Callable[[], Materia] = lambda: self._materia
        self.set_materia: Callable[[Materia], None] = lambda materia: setattr(self, '_materia', materia)
        self.estudiar: Callable[[], str] = lambda: f"Estudiando la materia {self._materia.get_nombre()}."
        self.ver_materia: Callable[[], str] = lambda: f"La materia es {self._materia.get_nombre()}."

    def __str__(self):
        return f"{super().__str__()}, Materia: {self.get_materia().get_nombre()}"

# Crear instancias
materia_matematicas = Materia("Matemáticas")
salario_docente = Salario(50000)

docente = Docente("Juan Pérez", 40, materia_matematicas, salario_docente)
estudiante = Estudiante("Ana Gómez", 20, materia_matematicas)

# Usar los métodos definidos con lambdas y __str__
print(docente)                        # Output: Nombre: Juan Pérez, Edad: 40, Materia: Matemáticas, Salario: 50000
print(estudiante)                     # Output: Nombre: Ana Gómez, Edad: 20, Materia: Matemáticas

# Usar getters y setters
docente.set_nombre("Carlos López")
print(docente.get_nombre())            # Output: Carlos López
docente.get_salario().set_cantidad(60000)
print(docente.ver_salario())           # Output: El salario es 60000

# Incrementar el salario del docente
nuevo_salario = docente.get_salario().incrementar(10)
print(nuevo_salario.get_cantidad())    # Output: 66000
print(nuevo_salario)                   # Output: Salario: 66000
