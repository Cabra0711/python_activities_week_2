#DATA_MARKET
products = []
total = 0 
total_expired = 0

amount = int(input("ingrese una cantidad: "))
products_expired = 0
for i in range(amount):
    product_name = input("Ingrese el nombre de su producto:")
    price = float(input("Escribe el precio de tu producto"))
    expired = input("El producto esta vencido? S/N").lower()
    if expired == "N":
        product = {"nombre": product_name, "Precio": price}
    products.append(product_name)
    total += price
else:
    products_expired +=1
    total_expired += price
print("\n--- RESUMEN FINAL---")
print(f"Se guardaron {len(products)}productos no vencidos")
print(f"El costo total de los productos no vencidos es: ${total:.2f}")
print(f"Productos vencidos: {products_expired}")
print(f"Costo total de productos vencidos: {total_expired}")
