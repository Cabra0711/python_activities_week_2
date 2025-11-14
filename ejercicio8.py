while True: 
    try:
        bills = int(input("Cuantas facturas deseas ingresar: "))
        if bills <= 0:
            print("Ingrese una cantidad valida!")
            continue
        break
    except ValueError:
        print("No puedes ingresar letras!")
for i in range(bills):
    c = i + 1
    print(f"\n--- PROCESANDO CLIENTE {c}---")
    while True:
            name = input("Ingrese el nombre del cliente: ")
            price = float(input("Ingrese el valor de su factura: "))
            bill_type = input("Digite el tipo de su factura: PREMIUM | NORMAL:  ").lower()
            if bill_type == "normal":
                desc = price*0.05
                print(f"Su factura se le aplico un descuento de el 5% por lo tanto queda en: {price-desc}")
            elif bill_type == "premium":
                desc = price*0.10
                print(f"Su factura se le aplico un descuento de el 10% por lo tanto queda en: {price-desc}")
            elif bill_type != "normal" and bill_type != "premium":
                print("Ingrese un valor entre los dos solicitados")
                continue
            break
