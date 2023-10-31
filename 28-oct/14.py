# 14. Una tienda de deportes vende pelotas de béisbol a $10 cada una, si se compran menos de 5, y a $14, si se compran 5 o más; se quiere saber el costo total de la compra, dependiendo del número de pelotas solicitadas.

def Tienda_Deportiva(e):
    if e < 5:
        return e * 10
    else:
       return e * 14
e = int(input("Ingrese la cantidad de pelotas que desea comprar: "))
costo_total = Tienda_Deportiva(e)
print("El costo total de la compra es: $", costo_total)

