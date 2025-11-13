large=[]
medium =[]
short= []
while True:
        try:
            print("==============BIENVENIDO A CINE COLOMBIA=============")
            movies = int(input("Digite la cantidad de peliculas que hay:"))
            if movies <=0:
                print("Ingrese una cantidad valida mayor a 0")
                continue
            break
        except ValueError:
            print("Ingrese un valor valido porfavor")
for i in range(movies):
        name = input("Ingrese el nombre de la pelicula: ")
        
        while True:
              try:
                duration = int(input("Digite la duracion de la pelicula: "))
                if duration <= 0:
                     print("Ingrese una duracion valida!!")
                     continue
                elif duration >=1 and duration <=100:
                    print(f"su pelicula es {name}la duracion de su pelicula es CORTA")
                    short.append(name)
                elif duration >=101 and duration <=149:
                    medium.append(name)
                    print(f"su peliucula es {name} la duracion de su pelicula es MEDIA")
                else:
                    large.append(name)
                    print(f"su pelicula es {name} la duracion de su pelicula es LARGA")
                break
              except ValueError:
                   print("Error vuelve a ingresar la pelicula y la duracion")
        