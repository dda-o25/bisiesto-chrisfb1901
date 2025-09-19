"""
Christian Alonso Flores Burgos

Fecha
19 de septiembre de 2025

Determinar si un año es bisiesto o no.

"""

# Declaraciones

# Entradas
año= int(input("Introduzca un año: "))

# Proceso 
if año % 4 != 0:
    print(año, "no es un año bisiesto")
else:
    if año % 100 != 0:
        print(año, "sí es un año bisiesto")
    else:
        if año % 400 == 0:
            print(año, "sí es un año bisiesto")
        else:
            print(año, "no es un año bisiesto")
