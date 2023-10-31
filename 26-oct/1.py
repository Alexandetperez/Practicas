import math

cateto1 = float(input("Ingrese el valor del primer cateto: "))
cateto2 = float(input("Ingrese el valor del segundo cateto: "))

area = cateto1 * cateto2 / 2
perimetro = cateto1 + cateto2 + math.sqrt(cateto1**2 + cateto2**2)

print("Área: ", area)
print("Perímetro: ", perimetro)