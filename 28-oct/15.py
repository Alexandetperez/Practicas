# 15. Indica si un número entero positivo es primo o no

def primo(n):
    if n <= 1:
        return False  # Los números menores o iguales a 1 no son primos
    if n <= 3:
        return True  # 2 y 3 son primos
    # Verificar divisibilidad por todos los números del 2 al número-1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # El número es divisible por i, por lo que no es primo
    return True  # Si no se encontraron divisores, el número es primo

numero = int(input("ingresa el numero: "))
if primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")
