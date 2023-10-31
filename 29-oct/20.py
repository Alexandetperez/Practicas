# 20. Realizar la lectura de una lista de números y determinar cuántos son positivos, y cuántos son negativos.

# Se Crea dos variables para contar los números positivos y negativos.
positivos = 0
negativos = 0

# Se Lee la lista de números separados por espacios.
num = input("Ingresa una lista de números: ")

# Se Convertierte la entrada en una lista de números.
num = num.split()

# Se itera a través de la lista de números.
for numero in num:
    # Convertir cada número a entero.
    numero = int(numero)
    
    # Determinar si el número es positivo negativo o cero.
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
# Se imprimir el resultado.
print("Cantidad de números positivos:", positivos)
print("Cantidad de números negativos:", negativos)
