'''3) Leer 10 números e imprimir solamente los números positivos
'''
num = 0 
contador = 1
while contador <= 10:
    num = int (input ("Ingresa un numero: "))
    if num > 0:
        print(f"El numero {num} es positivo:")
    contador = contador + 1
print ("FIN")