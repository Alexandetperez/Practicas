# Realiza un programa que efectúe la transformación de horas a minutos


def transform_h_m(horas):
  return horas * 60
horas = int(input("Ingrese el número de horas: "))
minutos = transform_h_m(horas)
print(f"{horas} horas son {minutos} minutos.")
