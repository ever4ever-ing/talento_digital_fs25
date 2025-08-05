import time

def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)#
        fin = time.time()
        print(f"La función '{func.__name__}' tardó {fin - inicio:.4f} segundos en ejecutarse.")
        return resultado
    return wrapper

@medir_tiempo
def funcion_lenta():
    time.sleep(2)
    print("Función lenta terminada.")

@medir_tiempo
def funcion_rapida(n):
    suma = 0
    for i in range(n):
        suma += i
    print(f"Suma de los primeros {n} números: {suma}")

if __name__ == "__main__":
    funcion_lenta()
    funcion_rapida(1000000)
