# 24. Elabora un programa que multiplique dos números enteros positivos utilizando sumas sucesivas (a x b, significa sumar b veces el número a), a y b se le piden al usuario.

# Se solicitan al usuario que ingrese dos números enteros positivos
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))

# Se verificar si los números ingresados son positivos
if a < 0 or b < 0:
    print("Por favor, ingresa números enteros positivos.")
else:
    # Se inicializar una variable para almacenar el resultado
    resultado = 0
    # Se multiplicar a por b utilizando sumas sucesivas
    for i in range(b):
        resultado += a
    # Se mostrar el resultado
    print(f"{a} x {b} = {resultado}")
