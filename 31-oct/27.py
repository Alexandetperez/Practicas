# 27. Desarrollar un programa que permita ingresar un vector de 10 elementos, e informe:
# - El valor acumulado de todos los elementos del vector.
# - El valor acumulado de los elementos del vector que sean mayores a 36.
# - Cantidad de valores mayores a 50.

# Crear un vector de 10 elementos
vector = []
# Pedir al usuario que ingrese los valores para el vector
for n in range(10):
    valor = int(input(f"Ingrese el valor {n + 1}: "))    
    vector.append(valor)
# Inicializar variables para almacenar los resultados
valor_acu= 0
valor_mayor_36 = 0
cantidad_mayor_50 = 0
# Calcular el valor acumulado y contar valores mayores a 50
for elemento in vector:
    valor_acu+= elemento
    if elemento > 36:
        valor_mayor_36 += elemento
    if elemento > 50:
        cantidad_mayor_50 += 1
# Mostrar los resultados
print(f"Valor acumulado de todos los elementos: {valor_acu}")
print(f"Valor acumulado de elementos mayores a 36: {valor_mayor_36}")
print(f"Cantidad de valores mayores a 50: {cantidad_mayor_50}")

