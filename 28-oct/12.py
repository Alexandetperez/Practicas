# 12. Los conjuntos deportivos tienen un precio de $500 cada uno si se compran menos de 3, y de 450 si se compran 3 o más. Obtener el total a pagar dependiendo del número de conjuntos a comprar.

def Conjunto_Deportivo(i):
  if i < 3:
    return i * 500
  else: return 3 * 500 +(i - 3) * 450
i = int(input("Ingrese el numero de conjuntos que quiere comprar: "))
print("El total a pagar es: $ ", Conjunto_Deportivo(i))