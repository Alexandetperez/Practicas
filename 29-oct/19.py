# 19. Calcular la suma de los primeros n números enteros positivos

# Pedimos al usuario que ingrese el valor de "n"
n = int(input("Ingrese un número entero positivo: "))
# Inicializamos una variable para almacenar la suma
suma_Pos = 0
# Verificamos que el valor de "n" sea un número entero positivo
if n <= 0:
    print("Por favor, ingrese un número entero positivo.")
else:
    # Utilizamos un bucle "for" para sumar los números enteros positivos desde 1 hasta "n"
    for e in range(1, n + 1):
        suma_Pos += e
    # Mostramos el resultado
    print(f"La suma de los primeros {n} números enteros positivos es: {suma_Pos}")