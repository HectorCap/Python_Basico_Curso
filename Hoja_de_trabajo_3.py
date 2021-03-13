# Héctor Oswaldo Ramón Cap Hernández

from colorama import Fore
'''
Ejercicio1
Escribir un programa que almacene una cadena de caracteres de contraseña en una variable, 
ingresada por el usuario, pregunte al usuario por la contraseña e imprima por pantalla si 
la contraseña introducida por el usuario coincide con la guardada en la variable sin tener 
en cuenta mayúsculas y minúsculas.
'''
contraseña = ""
contraseña = input("Ingrese su contraseña: ")

print()
print("Procesando...")
print()

contraseñaConfirma = ""
contraseñaConfirma = input("Por favor vuelva a ingresar su contraseña: ")

if (contraseña.lower() == contraseñaConfirma.lower()):
    print(Fore.LIGHTGREEN_EX+"Las contraseñas SÍ coinciden.")
else:
    print(Fore.RED+"Ups! Ocurrió un error, las contraseñas no coinciden.")

print(Fore.RESET)

# ---------------------------------------------------------------------------------------------------------

'''
Ejercicio2
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
El grupo A está formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre 
y sexo, y muestre por pantalla el grupo que le corresponde.
'''

nombre = input("Ingrese su nombre: ")
genero = input("Ingrese su genero: Si es hombre 'M' y si es mujer 'F' : ")

if (genero == "F"):
    if (nombre.lower() < "m"):
        grupo = "A"
    else:
        grupo = "B"
else:
    if (nombre.lower() > "n"):
        grupo = "A"
    else:
        grupo = "B"

if (genero == "F"):
    print(Fore.CYAN+"Bienvenida",nombre.upper(),"su grupo es", grupo,".")
    print(Fore.RESET)
else:
    print(Fore.CYAN+"Bienvenido",nombre.upper(),"su grupo es", grupo,".")
    print(Fore.RESET)