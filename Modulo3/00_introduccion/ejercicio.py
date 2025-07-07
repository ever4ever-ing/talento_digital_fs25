"""
Ingresar numero por teclado y mostrar si es par.
"""
import logging
# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
numero = int(input("Ingresa un numero: "))
logging.info("El numero ingresado es: %s", numero)
operacion = numero % 2
logging.debug("El resultado de la operacion es: %s", operacion)

if operacion == 0:
    print("El numero es Par")
else:
    print("El número no es par")