''' 4) Leer 20 números e imprimir cuantos son positivos,
 cuantos negativos y cuantos neutros.'''
num= 0
contador = 1
positivos = 0 
negativos = 0 
neutros = 0 
while contador <= 20:
    num = int (input ("Ingresa un numero: "))
    if num > 0 :
            positivos = positivos + 1
            contador = contador + 1
    print(f"El numero {num} es positivo")
        
    if num < 0 :
        negativos = negativos + 1
        contador
        print(f"El numero {num} es negativo")
       
    if num == 0 :
        neutros = neutros + 1
        print(f"El numero {num} es neutro")
        contador = contador + 1
        
print ("FIN")