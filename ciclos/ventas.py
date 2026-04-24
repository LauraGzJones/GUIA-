''' Una compañía de seguros tiene contratados a n vendedores. Cada uno hace tres ventas a la semana. 
Su política de pagos es que un
vendedor recibe un sueldo base, y un 10% extra por comisiones de sus ventas. 
El gerente de su compañía desea saber cuanto dinero
obtendrá en la semana cada vendedor por concepto de comisiones por las tres ventas realizadas, y cuanto tomando en cuenta su
sueldo base y sus comisiones.'''
n_vendedores = 0 
sueldo_base = 0
venta = 0
contador= 0

n_vendedores = int (input ("Ingrese el numero de vendedores: "))
sueldo_base = 500000
contador  = 1
comision = 0.10
total = 0 
venta = 0
while contador <= n_vendedores:

