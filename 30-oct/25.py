# 25. Elabora un programa que calcule la parte entera de la división de dos números enteros positivos utilizando restas sucesivas.

def division(divid, divisor):
  if divisor == 0:
    return "No se puede dividrir por cero"
  cocient=0
  while divid >= divisor:
    divid -= divisor
    cocient += 1
  return cocient
# Seingresan los numeros enteros para la division 
divid = int(input("Ingresa el dividendo: "))
divisor = int(input("Ingresa el divisor: "))
if divid < 0 or divisor < 0:
  print("Por favor ingresar numeros enteros ")
else:
  result = division(divid, divisor)
  print(f"La parte entera de {divid} dividido por {divisor} es: {result}")