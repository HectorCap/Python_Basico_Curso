# HÉCTOR OSWALDO RAMÓN CAP HERNÁNDEZ
# 201903910

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# EJERCICIO 1
Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.
Ejemplo 
El usuario ingresa el numero 5
*
**
***
****
*****
'''

print()
numero = int(input("Ingrese un número entero positivo para la altura de la pirámide: "))

if  (numero>0):
    print("Pirámide con altura de: ", numero)
    print()
    for i in range(numero):
        for j in range(i+1):
            print("*", end="")
        print()
else:
    print("El número ingresado no es un número entero positivo.")
print()

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
EJERCICIO 2
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.

Ejemplo
Usuario ingreso numero 6
6, 5, 4, 3, 2, 1, 0,
'''
numero = int(input("Ingrese un número entero positivo: "))

if  (numero > 0):
    for i in range(numero, -1, -1):
        print(i,",",end="")
    print()
else:
    print("El número ingresado no es un número entero positivo.")
print()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
# EJERCICIO 3
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''
numero = int(input("Ingrese un número entero positivo: "))

if (numero >0):
    contador = 0
    valor = True
    for i in range(1, numero+1):
        if (numero % i == 0):
            contador+=1
        if (contador > 2):
            valor = False
            break

    if (valor == True):
        print("El número ",numero," SÍ es un número primo")
    else:
        print("El número ",numero," NO es un número primo")
else:
    print("El número ingresado no es un número entero positivo.")

print()