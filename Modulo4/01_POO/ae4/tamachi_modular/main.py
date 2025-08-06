from tamagotchi import Tamagotchi
from persona import Persona

# Creando instancias y probando el funcionamiento
if __name__ == "__main__":
    # Crear una instancia de Tamagotchi
    mi_tamagotchi = Tamagotchi("Pikachu", "amarillo")

    # Crear una instancia de Persona y asignarle el Tamagotchi
    persona = Persona("Ana", 25, mi_tamagotchi)

    print(f"¡Hola! Soy {persona.nombre} y tengo {persona.edad} años.")
    print(
        f"Mi Tamagotchi se llama {persona.tamagotchi.nombre} y es de color {persona.tamagotchi.color}")

    # Mostrar estado inicial
    persona.tamagotchi.mostrar_estado()

    # La persona interactúa con su Tamagotchi
    print("=== Interacciones con el Tamagotchi ===")

    # Darle comida
    persona.darle_comida()

    # Jugar con él
    persona.jugar_con_tamagotchi()

    # Curarlo
    persona.curarlo()

    # Mostrar estado final
    persona.tamagotchi.mostrar_estado()

    # Más interacciones para ver los cambios
    print("=== Más interacciones ===")
    persona.jugar_con_tamagotchi()
    persona.darle_comida()
    persona.tamagotchi.mostrar_estado()
