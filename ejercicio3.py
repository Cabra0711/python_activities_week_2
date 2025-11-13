#GYM

points_accumulated = 0
while True:
    try:
        weeks = int(input("Cuantas semanas quieres registrar?"))
        if weeks <= 0 and weeks>=4:
            print("Numero invalido intente de nuevo porfavor")
            continue
        break
    except ValueError: 
        print("Vuelve a ingresar un dato valido:")
for i in range(weeks) :
    while True:
            try:
                days_trained = int(input("Ingresa los dias entrenados: "))
                if days_trained >7 :
                    print("Ingrese un valor valido entre 1 y 7.")
                elif days_trained <3 :
                    points_accumulated +=2
                    print("+2 PUNTOS puedes seguir mejorando!")
                elif days_trained >=3 and days_trained <=4:
                    points_accumulated +=5
                    print("+5 PUNTOS vas por buen camino!")
                elif days_trained >=5:
                    points_accumulated +=10
                    print("+10 PUNTOS EXCELENTE!!! SIGUE ASI!")
                    print(f"Tus puntos acumulados en estas semanas son:{points_accumulated}")
            except ValueError:
                print("Ingresa un valor valido.")
    
    
