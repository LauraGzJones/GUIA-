'''7) Calcular e imprimir la tabla de multiplicar de un número cualquiera. 
 Imprimir el multiplicando, el multiplicador y el producto.'''
num = 0 
contador = 0 
resultado = 0 
num = int( input ( "ingresa la  tabla  de multiplicar que deseas imprimir: "))
while contador <= 10:
    resultado =  num * contador 
    contador = contador + 1
    print(f"La multiplicación de {num} x {contador} = {resultado}")
 



