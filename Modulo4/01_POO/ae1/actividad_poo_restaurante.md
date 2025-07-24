# Modelado de un Sistema de Restaurante con Programación Orientada a Objetos (POO)


## 1. ¿Qué es la Orientación a Objetos y por qué es importante?
La Orientación a Objetos (OO) es un paradigma de programación que organiza el software en torno a "objetos", que representan entidades del mundo real. Permite estructurar el código de manera más clara, reutilizable y mantenible, facilitando la gestión de sistemas complejos como el de un restaurante.

**Ejemplo:**
- En un restaurante, puedes tener objetos como `Mesa`, `Cliente`, `Pedido` y `Plato`, cada uno con sus propios datos y comportamientos.

## 2. ¿Cómo puedes aplicar los conceptos de la Orientación a Objetos al sistema de un restaurante?
- **Clases:** Plantillas para crear objetos. Ejemplo: `Mesa`, `Pedido`, `Plato`.
- **Objetos:** Instancias de las clases. Ejemplo: una mesa específica (`mesa1`).
- **Atributos:** Características de cada clase. Ejemplo: `numero` y `capacidad` en `Mesa`.
- **Métodos:** Acciones que pueden realizar los objetos. Ejemplo: `ocupar()` en `Mesa`.

```python
class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
    def ocupar(self):
        self.ocupada = True
    def liberar(self):
        self.ocupada = False
```

```python
class Mesero:
    def __init__(self,nombre, horario):
        self.nombre = nombre
        self.horario= horario
        self.mesas_asignadas = []
    def tomar_pedido(self):
        pass
    def entregar_pedido(self):
        pass
    def cobrar_dinero(self):
        pass
    def asignar_mesa(self):
        pass
```

## 3. Definición de una Clase: Ejemplo de Cliente
Una clase en programación orientada a objetos es una plantilla que define cómo será un tipo de objeto, incluyendo sus características (atributos) y acciones (métodos). Por ejemplo, para modelar a un cliente en el sistema de un restaurante, podríamos crear una clase llamada Cliente que tenga atributos como nombre, teléfono y correo, y métodos para actualizar el teléfono o mostrar la información del cliente.

```python
class Cliente:
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono
    def hacer_reserva(self, mesa):
        # Lógica para reservar una mesa
    def actualizar_telefono(self,telefono):
        pass
```

## 4. Diferencia entre Clase, Instancia y Objeto
- **Clase:** Es el molde (ej: `Mesa`).
- **Instancia/Objeto:** Es el resultado de usar el molde (ej: `mesa1 = Mesa(1, 4)`).

## 5. ¿Qué son los Atributos de una Clase y cómo los usarías en un restaurante? Ejemplo en Pedido
```python
class Pedido:
    def __init__(self, numero, mesa, cliente):
        self.numero = numero
        self.mesa = mesa
        self.cliente = cliente
        self.platos = []
        self.estado = 'pendiente'
        self.costo_total = 0
```
Atributos relevantes: número, mesa, cliente, lista de platos, estado.

## 6. ¿Qué es el Estado de un Objeto y cómo lo afecta? Ejemplo en Mesa
El estado sería el conjunto de atributos en un momento determinado.

El estado de una mesa puede ser "libre" u "ocupada". Cambiar el estado afecta la disponibilidad en el sistema.

```python
mesa1 = Mesa(1, 4)
mesa1.ocupar()  # Estado cambia a ocupada
mesa1.liberar() # Estado cambia a libre
```

## 7. Diferencia entre Atributo y Estado
Estado es el valor actual y atributo puede cambiar o mantenerse.

- **Atributo:** Característica fija (ej: `capacidad`).
- **Estado:** Valor actual de un atributo (ej: `ocupada = True`).

## 8. Métodos de una Clase: Ejemplo en Reserva
```python
class Reserva:
    def realizar_reserva(self, cliente, mesa):
        # Lógica para reservar la mesa
        pass
```

## 9. Comportamiento de un Objeto: Ejemplo en Pedido
El comportamiento de un objeto está definido por sus métodos. Por ejemplo, un `Pedido` puede agregar platos y calcular el total.

```python
pedido1 = Pedido(1, mesa1, cliente1)
pedido1.agregar_plato(Plato("Hamburguesa", 8.5))
pedido1.calcular_total()
```

## 10. Diferencia entre Método y Comportamiento
- **Método:** Es una función definida en la clase (ej: `agregar_plato`).
- **Comportamiento:** Es el efecto de ejecutar uno o varios métodos (ej: el pedido suma platos y actualiza su total).

## 11. Principios Básicos de la POO
### Abstracción
Permite simplificar el sistema mostrando solo los detalles relevantes. Por ejemplo, la clase `Pedido` abstrae la lógica de gestión de platos y cálculo de total.

### Encapsulamiento
Consiste en proteger los datos internos de los objetos. Por ejemplo, los atributos de `Pedido` pueden ser privados y modificados solo mediante métodos:

```python
class Pedido:
    def __init__(self, numero):
        self.__numero = numero  # atributo privado
    def get_numero(self):
        return self.__numero
```

---

## Ejemplo completo en Python
```python
class Mesa:
    def __init__(self, numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.ocupada = False
    def ocupar(self):
        self.ocupada = True
    def liberar(self):
        self.ocupada = False

class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Pedido:
    def __init__(self, mesa):
        self.mesa = mesa
        self.platos = []
    def agregar_plato(self, plato):
        self.platos.append(plato)
    def calcular_total(self):
        return sum(plato.precio for plato in self.platos)

# Uso
mesa1 = Mesa(1, 4)
plato1 = Plato("Hamburguesa", 8.5)
plato2 = Plato("Ensalada", 5.0)
mesa1.ocupar()
pedido1 = Pedido(mesa1)
pedido1.agregar_plato(plato1)
pedido1.agregar_plato(plato2)
total = pedido1.calcular_total()
print(f"Total a pagar: ${total}")
mesa1.liberar()
```
