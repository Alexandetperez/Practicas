# 18. Dado un número, obtenga la sumatoria de dicho número. (La sumatoria de un número en está dada por la suma consecutiva de todos los números hasta n; por ejemplo: sumatoria de 3 es igual a sumar 3+2+1).

# función para obtener la sumatoria de un número
def numeros(num):
    # si el número es negativo, la sumatoria no existe
    if num < 0:
        return "La sumatoria no existe para números negativos"
    # si el número es 0, la sumatoria es 0
    elif num == 0:
        return 0
    # si el número es positivo, se suman todos los números desde 1 hasta el número (N)
    else:
        sum = 0
        for i in range(1, num + 1):
            sum += i
        return sum
numero = int(input("Ingrese un número: "))
print("La sumatoria del número ingresado es: ", numeros(numero))

