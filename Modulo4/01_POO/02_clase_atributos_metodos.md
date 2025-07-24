# Clase en Python: Atributos, Métodos, Colaboración y Composición

## 1. Creación de una clase en Python
Una clase es la estructura básica que define los objetos en Python. Incluye atributos (propiedades) y métodos (acciones) que los objetos de esa clase tendrán.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

## 2. Definición de atributos
Los atributos son variables que definen las características de un objeto. Se asignan en el constructor o pueden modificarse después.

```python
persona1 = Persona("Ana", 30)
print(persona1.nombre)  # Ana
```

## 3. Definición de métodos
Los métodos son funciones definidas dentro de una clase y permiten realizar acciones sobre los objetos.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, soy {self.nombre}")
```

## 4. Métodos accesores y mutadores
- **Accesores (getters):** Permiten obtener el valor de un atributo.
- **Mutadores (setters):** Permiten modificar el valor de un atributo.

```python
class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    def get_nombre(self):
        return self._nombre
    def set_nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
```

## 5. Método constructor
El constructor es el método especial `__init__` que inicializa los atributos del objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```


## 6. Sobrecarga de métodos en Python
En Python, la sobrecarga de métodos se simula usando argumentos opcionales, `*args` y `**kwargs`, ya que no permite definir varios métodos con el mismo nombre y diferente firma como en otros lenguajes.

### Ejemplo 1: Argumentos opcionales
```python
class Calculadora:
    def sumar(self, a, b, c=0):
        return a + b + c

calc = Calculadora()
print(calc.sumar(2, 3))      # 5
print(calc.sumar(2, 3, 4))   # 9
```

### Ejemplo 2: Usando *args
```python
class Calculadora:
    def sumar(self, *numeros):
        return sum(numeros)

calc = Calculadora()
print(calc.sumar(1, 2))           # 3
print(calc.sumar(1, 2, 3, 4, 5))  # 15
```

### Ejemplo 3: Usando **kwargs
```python
class Mensaje:
    def mostrar(self, **kwargs):
        if 'nombre' in kwargs and 'edad' in kwargs:
            print(f"Nombre: {kwargs['nombre']}, Edad: {kwargs['edad']}")
        elif 'nombre' in kwargs:
            print(f"Nombre: {kwargs['nombre']}")
        else:
            print("Sin datos")

m = Mensaje()
m.mostrar(nombre="Ana", edad=30)  # Nombre: Ana, Edad: 30
m.mostrar(nombre="Juan")           # Nombre: Juan
m.mostrar()                        # Sin datos
```

## 7. Colaboración entre objetos
La colaboración ocurre cuando un objeto utiliza métodos de otro para resolver una tarea.

```python
class Motor:
    def arrancar(self):
        print("Motor encendido")

class Auto:
    def __init__(self):
        self.motor = Motor()
    def encender(self):
        self.motor.arrancar()  # Colaboración
```

## 8. Composición de objetos
La composición es cuando un objeto "contiene" a otros objetos como atributos.

```python
class Rueda:
    def __init__(self, tipo):
        self.tipo = tipo

class Bicicleta:
    def __init__(self):
        self.rueda_delantera = Rueda("delantera")
        self.rueda_trasera = Rueda("trasera")
```

## 9. Diferencia entre colaboración y composición
- **Colaboración:** Objetos independientes interactúan para lograr un objetivo.
- **Composición:** Un objeto contiene a otros como parte de su estructura interna.

---

## Ejemplo práctico: Sistema de Mensajería Simple

### Problema: Modelar un sistema donde un Usuario puede enviar Mensajes a otro Usuario.

- Se utilizará colaboración (Usuario usa el método de Mensaje para enviar).
- Se utilizará composición (Buzon contiene Mensajes).

```python
class Mensaje:
    def __init__(self, texto, remitente, destinatario):
        self.texto = texto
        self.remitente = remitente
        self.destinatario = destinatario

class Buzon:
    def __init__(self):
        self.mensajes = []  # Composición: Buzon contiene Mensajes
    def recibir(self, mensaje):
        self.mensajes.append(mensaje)
    def mostrar(self):
        for m in self.mensajes:
            print(f"De: {m.remitente.nombre} - {m.texto}")

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.buzon = Buzon()  # Composición
    def enviar_mensaje(self, texto, destinatario):
        mensaje = Mensaje(texto, self, destinatario)
        destinatario.buzon.recibir(mensaje)  # Colaboración

# Uso
ana = Usuario("Ana")
juan = Usuario("Juan")
ana.enviar_mensaje("Hola Juan!", juan)
juan.buzon.mostrar()
```

**Salida esperada:**
```
De: Ana - Hola Juan!
```
