#Obtener fecha y hora actual del sistema

import datetime

ahora = datetime.datetime.now()

print(ahora) #Imprime con segundos y milisegundos 

print(type(ahora)) #saber tipo de dato

print(ahora.strftime('%d/%m/%Y/ %H:%M:%S')) # ajustamos los valores que queremos ver (formato)