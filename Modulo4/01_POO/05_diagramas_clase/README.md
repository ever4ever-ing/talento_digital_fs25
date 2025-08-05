# Ejemplo de Visibilidad de Atributos y Métodos en Python

Este ejemplo muestra cómo se implementan los niveles de visibilidad en Python usando una clase `CuentaBancaria` y una subclase `CuentaAhorro`.

## Niveles de Visibilidad

- **Público (+)**: El atributo o método es accesible desde cualquier lugar.
  - Se define normalmente, por ejemplo: `self.titular` o `def depositar(self, monto)`
- **Protegido (#)**: El atributo o método es accesible desde la clase y sus subclases.
  - Se define con un guion bajo: `self._saldo` o `def _verificar_saldo(self, monto)`
- **Privado (-)**: El atributo o método solo puede ser accedido desde dentro de la clase.
  - Se define con doble guion bajo: `self.__historial` o `def __registrar_operacion(self, operacion)`

## Clases

### CuentaBancaria
- **Atributos:**
  - `titular` (público)
  - `_saldo` (protegido)
  - `__historial` (privado)
- **Métodos:**
  - `depositar()` (público)
  - `_verificar_saldo()` (protegido)
  - `__registrar_operacion()` (privado)
  - `ver_historial()` (público)

### CuentaAhorro (hereda de CuentaBancaria)
- **Atributos:**
  - `tasa_interes` (público)
- **Métodos:**
  - `retirar()` (público, usa método protegido de la clase base)
  - `aplicar_interes()` (público, modifica atributo protegido)

## Ejemplo de Uso

```python
cuenta = CuentaAhorro("Juan Pérez", 1000, 0.05)
print(cuenta.titular)           # Acceso público
cuenta.depositar(500)           # Método público
print(cuenta._saldo)            # Acceso protegido (no recomendado fuera de la clase)
print(cuenta.__historial)       # Acceso privado (genera error)
print(cuenta.ver_historial())   # Acceso seguro al historial
cuenta.retirar(200)
cuenta.aplicar_interes()
```

## Notas
- En Python, la protección y privacidad son convenciones, no restricciones absolutas.
- Los atributos y métodos privados se renombran internamente (_name mangling_), por lo que no son accesibles directamente.
- Los atributos protegidos pueden ser accedidos desde fuera, pero no es recomendable.

---

Este ejemplo te ayuda a entender cómo organizar y proteger la información en tus clases usando la visibilidad adecuada.
