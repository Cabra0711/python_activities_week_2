while True:
    try:
        students = int(input("Ingrese la cantidad de estudiantes: "))
        if students <= 0:
            print("La cantidad de estudiantes debe ser un número positivo.")
            continue
        break
    except ValueError:
        print("Ingrese valores validos!!!!")

for i in range(students):
    print(f"\n--- Procesando Estudiante {i + 1} ---")
    
  
    name = input("Ingrese el nombre del estudiante: ")
    
    while True:
        try:
            qualification_1 = float(input("Ingrese nota 1 (de 1.0 a 5.0): "))
            if qualification_1 < 1 or qualification_1 > 5:
                print("Ingrese una nota entre 1.0 y 5.0")
                continue
            break
        except ValueError:
            print("Ingrese una nota valida porfavor!")


    while True:
        try:
            qualification_2 = float(input("Ingrese nota 2 (de 1.0 a 5.0): "))
            if qualification_2 < 1 or qualification_2 > 5:
                print("Ingrese una nota entre 1.0 y 5.0")
                continue
            break
        except ValueError:
            print("Ingrese una nota valida porfavor!")


    while True:
        try:
            qualification_3 = float(input("Ingrese nota 3 (de 1.0 a 5.0): "))
            if qualification_3 < 1 or qualification_3 > 5:
                print("Ingrese una nota entre 1.0 y 5.0")
                continue
            break
        except ValueError:
            print("Ingrese una nota valida porfavor!")
            
    total_average = (qualification_1 + qualification_2 + qualification_3) / 3
    
    print("---- RESUMEN-----")
    print(f"El nombre del estudiante es **{name}**")
    print(f"El promedio total es **{total_average:.2f}**")
    
    if total_average < 3.0:
        print("**REPROBADO**")
    else:
        print("**APROBADO**")