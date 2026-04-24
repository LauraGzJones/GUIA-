'''
 Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos. Realizar un algoritmo para calcular la calificación
media y la calificación mas baja de todo el grupo.'''

contador = 1        # variable que controla cuántas notas llevamos (1 a 3)
suma = 0            # acumulador para sumar todas las notas
menor = 0           # guardará la nota más baja

while contador <= 3:   # se repite 3 veces (3 alumnos)
    nota = float(input("Ingresa una nota: "))  # pide la nota al usuario
    
    suma = suma + nota   # suma la nota al total
    
    if contador == 1:    # en la primera vuelta
        menor = nota     # la primera nota se toma como la menor inicial
    else:
        if nota < menor: # en las siguientes, compara
            menor = nota # si es más pequeña, la guarda
    
    contador = contador + 1   # avanza al siguiente alumno

promedio = suma / 3   # calcula el promedio dividiendo por 3

print("Promedio:", promedio)      # muestra el promedio
print("Nota menor:", menor)       # muestra la nota más baja
     


     







