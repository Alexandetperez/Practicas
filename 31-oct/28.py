# 28. Desarrollar un programa que permita ingresar un vector de 15 elementos, e informe:
# - El menor número almacenado en el vector
# - El mayor número almacenado en el vector
#- El promedio de los números almacenados (esto si son 3 ejercicios pq son un poco más largos)

# Declaramos e inicializamos un vector de 15 elementos
vector = []
# Leemos los 15 elementos del vector
for e in range(15):
    num = int(input(f"Ingrese el elemento {e+1}: "))
    vector.append(num)
# Inicializamos las variables para almacenar el menor y mayor número, y el promedio de los números
menor = vector[0]
mayor = vector[0]
promedio = 0
# Iteramos sobre los elementos del vector para encontrar el menor y mayor número
for i in range(1, 15):
    if vector[i] < menor:
        menor = vector[i]
    elif vector[i] > mayor:
        mayor = vector[i]
# Calculamos el promedio de los números almacenados en el vector
for n in range(15):
    promedio += vector[n]
promedio /= 15
# Mostramos los resultados por pantalla
print(f"\nEl menor número almacenado en el vector es: {menor}")
print(f"El mayor número almacenado en el vector es: {mayor}")
print(f"El promedio de los números almacenados en el vector es: {promedio}")
