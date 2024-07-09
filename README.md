### README.md

# Python Advanced Concepts Practice

Este repositorio contiene ejemplos y prácticas de conceptos avanzados de Python, incluyendo el uso de Poetry como gestor de paquetes, creación de matrices y tensores usando list comprehensions, y clases en Python cuyos métodos están implementados con funciones lambda.

## Contenido

1. [Instalación](#instalación)
2. [Uso de Poetry](#uso-de-poetry)
3. [Creación de Matrices y Tensores](#creación-de-matrices-y-tensores)
4. [Clases con Métodos Lambda](#clases-con-métodos-lambda)
5. [Contribuir](#contribuir)
6. [Licencia](#licencia)

## Instalación

1. Clona este repositorio en tu máquina local.

   ```bash
   git clone https://github.com/tu-usuario/python-advanced-concepts.git
   cd python-advanced-concepts
   ```

2. Instala Poetry si no lo tienes instalado.

   ```bash
   pip install poetry
   ```

3. Instala las dependencias del proyecto usando Poetry.
   ```bash
   poetry install
   ```

## Uso de Poetry

Este proyecto utiliza Poetry para la gestión de dependencias y la configuración del entorno virtual.

### Instalación de Dependencias

Para instalar las dependencias definidas en `pyproject.toml`, usa:

```bash
poetry install
```

### Añadir Nuevas Dependencias

Para añadir una nueva dependencia, usa:

```bash
poetry add <nombre-dependencia>
```

### Ejecución de Scripts

Para ejecutar un script dentro del entorno virtual de Poetry, usa:

```bash
poetry run python <ruta-del-script>
```

## Creación de Matrices y Tensores

En el archivo `matrices_tensores.py`, se encuentran ejemplos de cómo crear matrices y tensores utilizando list comprehensions.

### Ejemplo de Matriz

```python
# Crear una matriz de 3x3
matriz = [[i + j for j in range(3)] for i in range(3)]
print(matriz)
# Output: [[0, 1, 2], [1, 2, 3], [2, 3, 4]]
```

### Ejemplo de Tensor

```python
# Crear un tensor 3x3x3
tensor = [[[i + j + k for k in range(3)] for j in range(3)] for i in range(3)]
print(tensor)
# Output: [[[0, 1, 2], [1, 2, 3], [2, 3, 4]], [[1, 2, 3], [2, 3, 4], [3, 4, 5]], [[2, 3, 4], [3, 4, 5], [4, 5, 6]]]
```

## Clases con Métodos Lambda

En el archivo `clases_lambda.py`, se encuentran ejemplos de cómo definir clases en Python cuyos métodos están implementados utilizando funciones lambda.

### Ejemplo de Clase `Persona`

```python
class Persona:
    def __init__(self, nombre: str, edad: int):
        self._nombre = nombre
        self._edad = edad
        self.get_nombre = lambda: self._nombre
        self.set_nombre = lambda nombre: setattr(self, '_nombre', nombre)
        self.get_edad = lambda: self._edad
        self.set_edad = lambda edad: setattr(self, '_edad', edad)
        self.presentarse = lambda: f"Hola, mi nombre es {self._nombre} y tengo {self._edad} años."

    def __str__(self):
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}"
```

### Ejemplo de Clase `Docente` que Hereda de `Persona`

```python
class Docente(Persona):
    def __init__(self, nombre: str, edad: int, materia: str, salario: float):
        super().__init__(nombre, edad)
        self._materia = materia
        self._salario = salario
        self.get_materia = lambda: self._materia
        self.set_materia = lambda materia: setattr(self, '_materia', materia)
        self.get_salario = lambda: self._salario
        self.set_salario = lambda salario: setattr(self, '_salario', salario)
        self.enseñar = lambda: f"Enseñando la materia {self._materia}."
        self.ver_salario = lambda: f"El salario es {self._salario}."

    def __str__(self):
        return f"{super().__str__()}, Materia: {self.get_materia()}, Salario: {self.get_salario()}"
```

### Ejemplo de Uso

```python
# Crear instancias
docente = Docente("Juan Pérez", 40, "Matemáticas", 50000)

# Usar los métodos definidos con lambdas
print(docente)  # Output: Nombre: Juan Pérez, Edad: 40, Materia: Matemáticas, Salario: 50000
print(docente.enseñar())  # Output: Enseñando la materia Matemáticas.
```

## Contribuir

¡Las contribuciones son bienvenidas! Por favor, abre un issue o envía un pull request con mejoras, correcciones o nuevas ideas.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ve el archivo [LICENSE](LICENSE) para más detalles.
