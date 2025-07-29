class TarjetaCredito:
    _UF = 39500
    _COSTO_MANTENCION_UF = 0.04

    def __init__(self, limite_credito=100000, intereses=0.0, saldo_pagar=0):
        # Usamos guion bajo para indicar que son atributos "protegidos"
        self._saldo_pagar = saldo_pagar + (self._UF * self._COSTO_MANTENCION_UF)
        self._limite_credito = limite_credito
        self._intereses = intereses
        print("Tarjeta creada con exito!")

    def compra(self, monto, cuotas):
        if self._saldo_pagar + monto > self._limite_credito:
            print("No puedes exceder el limite de credito")
        else: 
            if cuotas > 3:
                self._saldo_pagar += monto * (1 + self._intereses)
            else:
                self._saldo_pagar += monto  # sin interes
        return self

    def pago(self, monto):
        self._saldo_pagar -= monto
        return self

    def mostrar_info_tarjeta(self):
        print("\nMostrando informacion de tarjeta de Credito")
        print("=" * 20)
        print(f"Saldo a pagar: ${self._saldo_pagar:,.0f}")
        print(f"Limite de credito: ${self._limite_credito:,.0f}")
        print(f"Intereses: {self._intereses*100}%")
        print("=" * 20)
        return self

    def cobrar_interes(self):
        self._saldo_pagar += self._saldo_pagar * self._intereses
        return self

tarjeta1=TarjetaCredito(intereses=0.01)
tarjeta2=TarjetaCredito(limite_credito=200000,intereses=0.01)
tarjeta3=TarjetaCredito(limite_credito=150000,intereses=0.01)
tarjeta1.compra(15000,4).compra(30000,2).pago(20000).mostrar_info_tarjeta()
tarjeta2.compra(1000,1).compra(12000,2).compra(19000,4).pago(5000).pago(15000).mostrar_info_tarjeta()
tarjeta3.compra(10000,1).compra(20000,2).compra(10000,3).compra(65000,5).compra(50000,7).mostrar_info_tarjeta()
