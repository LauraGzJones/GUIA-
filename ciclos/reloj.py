''' 8) Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos de un día desde las 0:00:00 horas hasta las
23:59:59 horas'''

hora = 0 
minutos = 0 
segundos = 0

# Ciclo de horas (de 0 a 23)
while hora <= 23:
    
    # Ciclo de minutos (de 0 a 59)
    while minutos <= 59:
        
        # Ciclo de segundos (de 0 a 59)
        while segundos <= 59: 
            # Imprime la hora actual en formato hh:mm:ss
            print(f"{hora}:{minutos}:{segundos}")
            
            # Aumenta los segundos en 1
            segundos = segundos + 1  
        
        # Cuando los segundos llegan a 59, se reinician a 0
        # y se aumenta un minuto
        minutos = minutos + 1
        segundos = 0                                                
    
    # Cuando los minutos llegan a 59, se reinician a 0
    # y se aumenta una hora
    hora = hora + 1
    minutos = 0                 
    
    # Se reinician los segundos para la nueva hora
    segundos = 0
    