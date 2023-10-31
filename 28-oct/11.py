# 11. Calcular el precio de un boleto de ida y vuelta en ferrocarril, conociendo la distancia del viaje de ida y el tiempo de estancia. Se sabe, además, que si el número de días de estancia es superior a 7 y la distancia total (ida y vuelta) a recorrer es superior a 800 km, el boleto tiene un descuento del 30%. El precio por kilómetro es $0.25

# Variables de entrada
distancia_ida = float(input("Ingrese la distancia del viaje de ida en km: "))
distancia_vuelta = float(input("Ingrese la distancia del viaje de vuelta en km: "))
tiempo_estancia = int(input("Ingrese el tiempo de estancia en días: "))

# Calcular la distancia total del viaje
distancia_total = distancia_ida + distancia_vuelta

# Determinar si se aplica el descuento
descuento = 0
if tiempo_estancia > 7 and distancia_total > 800:
    descuento = 0.3

# Calcular el precio del boleto
precio_boleto = distancia_total * 0.25
precio_boleto -= precio_boleto * descuento

# Imprimir el resultado
print("El precio del boleto de ida y vuelta es: $", round(precio_boleto, 2))