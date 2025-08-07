class MiErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
try:
    raise MiErrorPersonalizado("Este es un error personalizado")
except MiErrorPersonalizado as e:
    print(f"Se ha capturado un error: {e}")
