# 26. Elabora un programa que calculé el promedio de calificación de matemáticas para un grupo de 50 alumnos.

# Inicializamos una lista vacía para almacenar las calificaciones de matemáticas
calificaciones_matematicas = []

# Pedimos al usuario que ingrese las calificaciones de matemáticas para 50 alumnos
for n in range(50):
    calificacion = float(input(f"Ingrese la calificación de matemáticas del alumno {n+1}: "))
    calificaciones_matematicas.append(calificacion)

# Calculamos el promedio de las calificaciones de matemáticas
promedio = sum(calificaciones_matematicas) / len(calificaciones_matematicas)

# Mostramos el promedio de las calificaciones de matemáticas
print(f"El promedio de las calificaciones de matemáticas para 50 alumnos es: {promedio}")