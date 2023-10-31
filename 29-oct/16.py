# 16. Obtener la suma de todos los números enteros pares y la suma de los números impares comprendidos entre 1 y N, en donde N es un entero positivo.

def números (n): 
   suma_pares = 0
   suma_impares = 0
   for i in range(1, n+1): 
       if i % 2 == 0: 
           suma_pares += i
       else: 
           suma_impares += i
   return (suma_pares, suma_impares)