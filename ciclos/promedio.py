'''EJERCICIOS PROPUESTOS DE CICLOS
1) Calcular el promedio de un alumno que tiene 7 calificaciones en la materia de Diseño Estructurado de Algoritmos
2) Leer 10 números y obtener su cubo y su cuarta.
3) Leer 10 números e imprimir solamente los números positivos
4) Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros.
5) Leer 15 números negativos y convertirlos a positivos e imprimir dichos números.
6) Suponga que se tiene un conjunto de calificaciones de un grupo de 40 alumnos. Realizar un algoritmo para calcular la calificación
media y la calificación mas baja de todo el grupo.
7) Calcular e imprimir la tabla de multiplicar de un número cualquiera. Imprimir el multiplicando, el multiplicador y el producto.
8) Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos de un día desde las 0:00:00 horas hasta las
23:59:59 horas
9) Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a la semana. Su política de pagos es que un
vendedor recibe un sueldo base, y un 10% extra por comisiones de sus ventas. El gerente de su compañía desea saber cuanto dinero
obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas realizadas, y cuanto tomando en cuenta su
sueldo base y sus comisiones.
10) En una empresa se requiere calcular el salario semanal de cada uno de los n obreros que laboran en ella. El salario se obtiene de la
siguiente forma:
Si el obrero trabaja 40 horas o menos se le paga $20 por hora'''


#1) Calcular el promedio de un alumno que tiene 
# 7 calificaciones en la materia de Diseño Estructurado de Algoritmos

calificaciones = 0 
suma =0 

ciclo = 1
promedio = 0
while ciclo <= 7 :
     calificaciones = float(input ("Ingresa la calificaciones para calcular el promedio:")) 
     ciclo = ciclo + 1
     suma = suma + calificaciones

else :
        promedio = suma / 7
        print(f"El promedio de calificaciones es:{promedio}")
    
