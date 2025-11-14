normal= 0
express = 0
urgent = 0
while True:
    try:
        amount = int(input("Ingresa la cantidad de paquetes: "))
        if amount <= 0 :
            print("Ingrese una cantidad valida")
            continue
        break
    except ValueError:

        print("Digite solamente numeros!!")
for i in range(amount):
    c = i + 1
    choose_a_type = input(f"Escoge un tipo de paquete {i+1}: NORMAL | EXPRESS | URGENTE |").lower().upper()
    if choose_a_type == "NORMAL" :
        normal += 1
        print("Se ha añadido un paquete a tu NORMAL")
    elif choose_a_type == "EXPRESS":
        express += 1   
        print("Se ha añadido un paquete a tu EXPRESS")
    elif choose_a_type == "URGENTE":
        urgent += 1
    else: 
        print("tipo de paquete.No reconocidos")
print(f"La cantidad de paquetes que asignaste es de: {urgent} Normal: {normal} Express: {express}")
