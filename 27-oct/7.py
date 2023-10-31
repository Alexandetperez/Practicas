# Realiza el promedio de 4 calificaciones de una misma materia.

def prom_materia(materia):
  calif1 = float(input("Ingrese la primera calificación: "))
  calif2 = float(input("Ingrese la segunda calificación: "))
  calif3 = float(input("Ingrese la tercera calificación: "))
  calif4 = float(input("Ingrese la cuarta calificación: "))
  promedio = (calif1 + calif2 + calif3 + calif4) / 4
  return f"El promedio de {materia} es: {promedio}"
