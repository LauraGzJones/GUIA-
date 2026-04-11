# 1. Crear un algoritmo en diagrama de flujo que al leer un número entero positivo (asuma que el número cumple las condiciones),
#imprimir PAR si el número es par e IMPAR si es impar.

n = 0 
n= int (input ( "Ingresa un numero para verificar si este es par o impar: "))
# % este es el resto de una deivision lo que sgnifica q  es para 

if n% 2 == 0:      
    print( " El numero seria par")
else:
    print("El numero seria impar ")



