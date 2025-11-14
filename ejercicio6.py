TOTAL_HOUR = 20000
TOTAL_PART= 50000
while True: 
    try:
        amount_cars = int(input("Ingrese la cantidad de carros"))
        if amount_cars <=0:
            print("Ingrese una cantidad de carros valida")
            continue
        break
    except ValueError:
        print("Valor invalido intente de nuevo.")
for i in range(amount_cars):
    print(f"\n--- Procesando carro {i + 1} ---")
    while True:
        try:
            total_hours = int(input("Cuantas horas de trabajo trabajaste hoy:"))
            total_parts = int(input("Cuantas piezas cambiaste hoy:"))
            if total_hours <= 0 and total_parts <= 0:
                print("Ingrese una cantidad de piezas y horas valida")
                continue 
            elif total_hours >10 or total_parts >4:
                complexity = "Actividad Compleja"
            else:
                complexity = "Actividad normal"
            break
        except ValueError:
            print("Ingrese valores validos porfavor!!!")
    vehicle_cost = (TOTAL_HOUR * total_hours) + (TOTAL_PART * total_parts)
    print(f"El costo de su vehiculo es: {vehicle_cost} y la complejidad es: {complexity}")