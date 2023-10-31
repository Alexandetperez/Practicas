# 13. Una escuela tiene el siguiente problema: si el alumno obtiene una calificación de menos de 65 puntos no aprobará el curso, en otro caso lo aprobará. Pedir la nota al usuario

nota = int(input("Indroduce la nota: "))
if nota < 65:
  print("No aprobaste el curso")
else:
  print("Aprobaste el curso")