''' ) Leer 10 número y obtener su cubo y su cuarta.'''
num = 0
cubo =0
cuarta = 0
contador = 1
while contador <= 10 :
    num = int(input ("Ingresa un numero para obtener su cubo y su cuarta :"))
    cubo = num * num * num
    cuarta = num * num * num * num
    print(f"El cubo de {num} es {cubo } y la cuarta es {cuarta}")
    contador = contador + 1
print ("Fin del programa")