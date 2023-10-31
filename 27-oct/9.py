#  Convertir una cantidad de metros a kilómetros, centímetros, milímetros y millas, según selección del usuario.
def metros_a_kilometros(cantidad_metros):
    return cantidad_metros / 1000

def metros_a_centimetros(cantidad_metros):
    return cantidad_metros * 100

def metros_a_milimetros(cantidad_metros):
    return cantidad_metros * 1000

def metros_a_millas(cantidad_metros):
    return cantidad_metros / 1609.34

cantidad_metros = float(input("Ingresa una cantidad en metros: "))
opcion = int(input("Selecciona la unidad a la que deseas convertir:\n1. Kilómetros\n2. Centímetros\n3. Milímetros\n4. Millas\n"))

if opcion == 1:
    resultado = metros_a_kilometros(cantidad_metros)
    print(f"{cantidad_metros} metros son {resultado} kilómetros.")
elif opcion == 2:
    resultado = metros_a_centimetros(cantidad_metros)
    print(f"{cantidad_metros} metros son {resultado} centímetros.")
elif opcion == 3:
    resultado = metros_a_milimetros(cantidad_metros)
    print(f"{cantidad_metros} metros son {resultado} milímetros.")
elif opcion == 4:
    resultado = metros_a_millas(cantidad_metros)
    print(f"{cantidad_metros} metros son {resultado} millas.")
else:
    print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
