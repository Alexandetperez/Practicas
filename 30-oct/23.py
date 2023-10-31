# 23. Solicitar al usuario el ingreso de una contraseña desde el teclado. El programa deberá continuar su ejecución hasta que la contraseña sea correcta.

# Definir la contraseña correcta
contrasena_correcta = "18Sep.1998"
# Solicitar la contraseña al usuario
while True:
    contrasena_ingresar = input("Por favor, ingrese la contraseña: ")
    # Verificar si la contraseña ingresada es correcta
    if contrasena_ingresar == contrasena_correcta:
        print("¡Contraseña correcta!.")
        break
    else:
        print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
