#  Aplicar un aumento de 15% a un trabajador si su sueldo es inferior a $1000 mensuales y 12% en caso contrario.

sueldo = float(input("Ingrese el sueldo mensual del trabajador: "))

if sueldo < 1000:
    aumento = sueldo * 0.15  
else:
    aumento = sueldo * 0.12 

nuevo_sueldo = sueldo + aumento

print(f"El nuevo sueldo del trabajador es: ${nuevo_sueldo:.2f}")

