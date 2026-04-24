'''Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
'''

num = -0
contador= 0 
positivo = 0 

while  contador <=15:
    num = int (input( "Ingresa un numero: "))
    if num < 0:
         positivo = num * -1
       
         print (f"Los numeros en positivo: {positivo}")
    
    contador = contador + 1

print ("Solo números negativos ")
        






