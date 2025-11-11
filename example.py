animals = ["perro", "gato", "conejo", "caballo"]
print("Lista inicial de animales:", animals)

while True:
    new_animal = input("Ingresa un nuevo animal: ")
    animals.append(new_animal)
    print("Lista actualizada:", animals)

    respuesta = input("¿Deseas añadir un nuevo animal? (si/no): ").lower()

    if respuesta == "no":
        borrar = input("¿Deseas borrar un animal? (si/no): ").lower()
        if borrar == "si":
            borrar_animal = input("¿Qué animal deseas borrar?: ").lower()
            if borrar_animal in animals:
                animals.remove(borrar_animal)
                print("Animal eliminado. Lista actual:", animals)
            else:
                print("Ese animal no está en la lista.")
        print("Programa finalizado. Lista final:", animals)
        break  