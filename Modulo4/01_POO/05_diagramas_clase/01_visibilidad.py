class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        # Atributos públicos (se acceden desde cualquier lugar)
        self.titular = titular  # + público
        # Atributos protegidos (se acceden desde la clase y subclases)
        self._saldo = saldo_inicial  # # protegido
        
        # Atributos privados (solo se acceden desde dentro de la clase)
        self.__historial = []  # - privado
    
    # Método público
    def depositar(self, monto):

        """+ público: Puede ser llamado desde cualquier lugar"""
        if monto > 0:
            self._saldo += monto
            self.__registrar_operacion(f"Depósito: +${monto}")
            return True
        return False
    
    # Método protegido
    def _verificar_saldo(self, monto):
        """# protegido: Solo accesible desde la clase y subclases"""
        return self._saldo >= monto
    
    # Método privado
    def __registrar_operacion(self, operacion):
        """- privado: Solo accesible desde dentro de la clase"""
        self.__historial.append(operacion)
    
    # Método público para ver el historial
    def ver_historial(self):
        """+ público: Permite ver el historial de manera segura"""
        return self.__historial.copy()  # Devuelve una copia para proteger el original

# Clase que hereda de CuentaBancaria
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo_inicial, tasa_interes):
        super().__init__(titular, saldo_inicial)
        self.tasa_interes = tasa_interes  # + público
    
    def retirar(self, monto):
        """Ejemplo de uso de método protegido heredado"""
        if self._verificar_saldo(monto):  # Puede usar _verificar_saldo por ser subclase
            self._saldo -= monto
            return True
        return False
    
    def aplicar_interes(self):
        """Ejemplo de modificación de atributo protegido"""
        interes = self._saldo * self.tasa_interes
        self._saldo += interes


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cuenta de ahorro
    cuenta = CuentaAhorro("Juan Pérez", 1000, 0.05)
    
    # Acceso a atributos y métodos públicos (funciona )
    print(f"Titular: {cuenta.titular}")
    cuenta.depositar(500)
    
    # Acceso a atributos y métodos protegidos 
    # (funciona, pero Python advierte que no deberíamos hacerlo)
    print(f"Saldo actual: ${cuenta._saldo}")
    
    # Intentar acceder a atributos y métodos privados 
    # (generará un error)
    try:
        print(cuenta.__historial)  # Esto generará un error
    except AttributeError as e:
        print(f"Error al acceder al historial privado: {e}")
    
    # Forma correcta de ver el historial (a través del método público)
    print("\nHistorial de operaciones:")
    for operacion in cuenta.ver_historial():
        print(operacion)
    
    # Probar la cuenta de ahorro
    cuenta.retirar(200)
    cuenta.aplicar_interes()
    print(f"\nSaldo después de retiro e intereses: ${cuenta._saldo}")
