class TarjetaCredito:
    banco = "Banco Internacional de Programadores"
    todas_las_tarjetas = []

    def __init__(self, saldo_pagar, limite_credito=100000, tasa_interes=0.02):
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
        self.tasa_interes = tasa_interes
        TarjetaCredito.todas_las_tarjetas.append(self)
    @classmethod
    def cambiar_banco(cls, nombre):
        cls.banco = nombre
    @classmethod
    def todos_saldos(cls):
        total_saldos = 0
        for tarjeta in cls.todas_las_tarjetas:  # Usamos cls para hacer referencia a la clase
            total_saldos += tarjeta.saldo_pagar
        return total_saldos
    
    @staticmethod
    def puede_comprar(limite, saldo_utilizado, monto):
        #Revisamos si con la compra, el saldo sobrepasa el límite de crédito
        if (saldo_utilizado + monto) > limite:
            return False
        else:
            return True
        
    def hacer_compra(self, monto):
        if TarjetaCredito.puede_comprar(self.limite_credito, self.saldo_pagar, monto):
            self.saldo_pagar += monto
        else:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        return self
   
   