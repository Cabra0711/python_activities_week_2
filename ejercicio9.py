free_rooms = 0
unavaible_rooms = 0
free_roomss_list = []
while True:
    try:
        rooms = int(input("Ingrese el numero de habitaciones: "))
        if rooms <= 0:
            print("Vuelva a digitar las habitaciones.")
            continue
        break
    except ValueError:
        print("Ingrese un numero valido porfavor!!")
for i in range(rooms):
    room_number = int(input("Digite el numero de la habitacion: "))
    romm_taken = input("La habitacion esta ocupada? si/no: ").lower()
    if romm_taken == "si":
        unavaible_rooms += 1
        print("La habitacion que digitaste esta ocupada.")
    elif romm_taken == "no":
        free_rooms += 1
        free_roomss_list.append(room_number)
        print("La habitacion digitada esta disponible.")
print("----RESUMEN----")
print(f"La cantidad de habitaciones disponibles son: {free_rooms} Ocupadas: {unavaible_rooms}")
print(f"Las habitaciones disponibles es: {free_roomss_list}")
print("Gracias por visitarnos!!")