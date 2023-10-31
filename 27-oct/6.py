# Transforma en metros a centímetro.

def transforma_m_cm(m):
  cm = m * 100
  return cm
metros = float(input("Ingrese la cantidad de metros: "))
centimetros = transforma_m_cm(metros)
print(f"{metros} metros es igual a {centimetros} centímetros.")

