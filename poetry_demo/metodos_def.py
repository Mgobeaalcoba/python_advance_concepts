from typing import Type

class Persona:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def get_edad(self) -> int:
        return self._edad

    def set_edad(self, edad: int) -> None:
        self._edad = edad

    def presentarse(self) -> str:
        return f"Hola, mi nombre es {self._nombre} y tengo {self._edad} años."

    def __str__(self) -> str:
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}"

class Materia:
    def __init__(self, nombre: str):
        self._nombre = nombre

    def get_nombre(self) -> str:
        return self._nombre

    def set_nombre(self, nombre: str) -> None:
        self._nombre = nombre

    def __str__(self) -> str:
        return f"Materia: {self.get_nombre()}"

class Salario:
    def __init__(self, cantidad: float):
        self._cantidad = cantidad

    def get_cantidad(self) -> float:
        return self._cantidad

    def set_cantidad(self, cantidad: float) -> None:
        self._cantidad = cantidad

    def incrementar(self, porcentaje: float) -> 'Salario':
        return Salario(self._cantidad * (1 + porcentaje / 100))

    def __str__(self) -> str:
        return f"Salario: {self.get_cantidad()}"

class Docente(Persona):
    def __init__(self, nombre: str, edad: int, materia: Type[Materia], salario: Type[Salario]):
        super().__init__(nombre, edad)
        self._materia = materia
        self._salario = salario

    def get_materia(self) -> Materia:
        return self._materia

    def set_materia(self, materia: Materia) -> None:
        self._materia = materia

    def get_salario(self) -> Salario:
        return self._salario

    def set_salario(self, salario: Salario) -> None:
        self._salario = salario

    def enseñar(self) -> str:
        return f"Enseñando la materia {self._materia.get_nombre()}."

    def ver_salario(self) -> str:
        return f"El salario es {self._salario.get_cantidad()}."

    def __str__(self) -> str:
        return f"{super().__str__()}, Materia: {self.get_materia().get_nombre()}, Salario: {self.get_salario().get_cantidad()}"

class Estudiante(Persona):
    def __init__(self, nombre: str, edad: int, materia: Type[Materia]):
        super().__init__(nombre, edad)
        self._materia = materia

    def get_materia(self) -> Materia:
        return self._materia

    def set_materia(self, materia: Materia) -> None:
        self._materia = materia

    def estudiar(self) -> str:
        return f"Estudiando la materia {self._materia.get_nombre()}."

    def ver_materia(self) -> str:
        return f"La materia es {self._materia.get_nombre()}."

    def __str__(self) -> str:
        return f"{super().__str__()}, Materia: {self.get_materia().get_nombre()}"

# Crear instancias
materia_matematicas = Materia("Matemáticas")
salario_docente = Salario(50000)

docente = Docente("Juan Pérez", 40, materia_matematicas, salario_docente)
estudiante = Estudiante("Ana Gómez", 20, materia_matematicas)

# Usar los métodos
print(docente)                        # Output: Nombre: Juan Pérez, Edad: 40, Materia: Matemáticas, Salario: 50000
print(estudiante)                     # Output: Nombre: Ana Gómez, Edad: 20, Materia: Matemáticas

# Usar getters y setters
docente.set_nombre("Carlos López")
print(docente.get_nombre())            # Output: Carlos López
docente
