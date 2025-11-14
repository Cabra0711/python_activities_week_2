while True:
    try:
        employees = int(input("Ingrese la cantidad de trabajadores: "))
        if employees <= 0:
            print("Ingrese una cantidad de trabajadores porfavor.")
            continue
        break
    except ValueError:
        print("Solo valores validos porfavor!!")
for i in range(employees):
    name = input("Ingrese el nombre de el empleado: ")
    sells_1 = int(input("Ingresa la cantidad de ventas en el mes: "))
    if sells_1 < 3 : 
        print("Bajo rendimiento")
    elif sells_1 >= 3 and sells_1 <= 5 :
        print("Bien!!")
    elif sells_1 >= 6:
        print("Excelente")
while True:
    try:
        sells_2 = int(input("Ingresa la cantidad de ventas en el mes: "))
        if sells_2 <= 0: 
            print("Cantidad invalida vuelva a digitar porfavor")
            continue
        if sells_2 < 3 : 
            print("Bajo rendimiento")
        elif sells_2 >= 3 and sells_2 <= 5 :
            print("Bien!!")
        elif sells_2 >= 6:
            print("Excelente")
        break
    except ValueError:
        print("Ingrese valores validos porfavor!!")

while True:
    try:
        sells_3 = int(input("Ingresa la cantidad de ventas en el mes: "))
        if sells_3 <= 0: 
            print("Cantidad invalida vuelva a digitar porfavor")
            continue
        if sells_3 < 3 : 
            print("Bajo rendimiento")
        elif sells_3 >= 3 and sells_3 <= 5 :
            print("Bien!!")
        elif sells_3 >= 6:
            print("Excelente")
        break
    except ValueError:
        print("Ingrese valores validos porfavor!!")
average = (sells_1 + sells_2 + sells_3)/3
if average < 3 : 
    print("Bajo rendimiento")
elif average >= 3 and average <= 5 :
            print("Bien!!")
elif average >= 6:
    print("Excelente")

print(f"---RESUMEN---")
print(f"El nombre es: {name} y la calificacion es {average}")