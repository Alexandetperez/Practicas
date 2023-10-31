# 21. Imprimir la lista de números pares que se encuentran contenidos entre los números a y b, los cuales se le piden al usuario.

# Se pedin al usuario que ingrese los números a y b
a = int(input("Ingresa el número a: "))
b = int(input("Ingresa el número b: "))
# Se asegurarse de que a sea menor que b
if a > b:
    a, b = b, a
# Se imprimen los números pares en el rango [a, b]
print(f"Los números pares entre {a} y {b} son:")
for numero in range(a, b + 1):
    if numero % 2 == 0:
        print(numero)
