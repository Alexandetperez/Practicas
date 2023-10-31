# 22. Modifica el ejercicio anterior para que imprima los números impares.

# Se pedin al usuario que ingrese los números a y b
a = int(input("Ingresa el número a: "))
b = int(input("Ingresa el número b: "))
# Se asegurarse de que a sea menor que b
if a > b:
    a, b = b, a
# Se imprimen los números pares en el rango [a, b]
print(f"Los números impares entre {a} y {b} son:")
for numero in range(a, b + 1):
    if numero % 2 != 0:  # Se verifica si el número es impar
        print(numero)