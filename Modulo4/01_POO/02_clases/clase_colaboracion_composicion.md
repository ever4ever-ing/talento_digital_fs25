# Clase en Python: Atributos, Métodos, Colaboración y Composición

## Introducción
En Python, una clase es la estructura básica para definir objetos. Los objetos tienen atributos (propiedades) y métodos (acciones). Además, los objetos pueden colaborar entre sí y pueden estar compuestos por otros objetos.

---

## 1. Creación de una clase en Python
```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
```

## 2. Definición de atributos
Los atributos definen las características de un objeto. Se asignan en el constructor o pueden modificarse después.

```python
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry")
print(libro1.titulo)  # El Principito
```

## 3. Definición de métodos
Los métodos son funciones dentro de una clase que permiten realizar acciones sobre los objetos.

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    def descripcion(self):
        return f"{self.titulo} de {self.autor}"
```

## 4. Métodos accesores y mutadores
- **Accesores (getters):** Permiten obtener el valor de un atributo.
- **Mutadores (setters):** Permiten modificar el valor de un atributo.

```python
class Libro:
    def __init__(self, titulo, autor):
        self._titulo = titulo
        self._autor = autor
    def get_titulo(self):
        return self._titulo
    def set_titulo(self, nuevo_titulo):
        self._titulo = nuevo_titulo
```

## 5. Método constructor
El constructor es el método especial `__init__` que inicializa los atributos del objeto.

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
```

## 6. Sobrecarga de métodos en Python
En Python, la sobrecarga de métodos se simula usando argumentos opcionales o `*args` y `**kwargs`.

```python
class Calculadora:
    def sumar(self, a, b, c=0):
        return a + b + c
```

## 7. Colaboración entre objetos
La colaboración ocurre cuando un objeto utiliza métodos de otro para resolver una tarea.

```python
class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
    def presentar(self):
        return f"Autor: {self.nombre}"

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor  # Colaboración: Libro usa un objeto Autor
    def descripcion_completa(self):
        return f"{self.titulo} - {self.autor.presentar()}"

# Uso
autor1 = Autor("Gabriel García Márquez")
libro1 = Libro("Cien años de soledad", autor1)
print(libro1.descripcion_completa())
```

## 8. Composición de objetos
La composición es cuando un objeto contiene a otros objetos como atributos.

```python
class Pagina:
    def __init__(self, numero, contenido):
        self.numero = numero
        self.contenido = contenido

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.paginas = []  # Composición: Libro contiene páginas
    def agregar_pagina(self, pagina):
        self.paginas.append(pagina)
```

## 9. Diferencia entre colaboración y composición
- **Colaboración:** Objetos independientes interactúan para lograr un objetivo.
- **Composición:** Un objeto contiene a otros como parte de su estructura interna.

---

## Ejemplo práctico: Biblioteca Simple

### Problema: Modelar una biblioteca donde un Usuario puede pedir prestado un Libro.
- Se utiliza colaboración (Usuario usa el método de Libro para pedir prestado).
- Se utiliza composición (Biblioteca contiene Libros).

```python
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False
    def prestar(self):
        if not self.prestado:
            self.prestado = True
            return True
        return False
    def devolver(self):
        self.prestado = False

class Biblioteca:
    def __init__(self):
        self.libros = []  # Composición: Biblioteca contiene Libros
    def agregar_libro(self, libro):
        self.libros.append(libro)
    def mostrar_libros(self):
        for libro in self.libros:
            estado = "Prestado" if libro.prestado else "Disponible"
            print(f"{libro.titulo} - {estado}")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
    def pedir_libro(self, libro):
        if libro.prestar():
            print(f"{self.nombre} ha prestado '{libro.titulo}'")
        else:
            print(f"'{libro.titulo}' no está disponible")

# Uso
biblioteca = Biblioteca()
libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Fahrenheit 451", "Ray Bradbury")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
usuario1 = Usuario("Ana")
usuario1.pedir_libro(libro1)
biblioteca.mostrar_libros()
```

**Salida esperada:**
```
Ana ha prestado '1984'
1984 - Prestado
Fahrenheit 451 - Disponible
```
