#B. Desarrolle un programa que permita ingresar un número, 
# si es negativo debemos enviar un mensaje al usuario “Número inválido, 
# reingrese” y debe volver a ingresar otro número, si es positivo enviamos un mensaje 
# “Número correcto” y termina el programa.

n = -1
n = int(input ( "Ingresa un numero: "))
if n < 0 :
     n = int(input("Numero invalido reingrese"))
else :
     print("Numero correcto")     
