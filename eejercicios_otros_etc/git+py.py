print('definitivo final')

#calcular la diferencia en dias de 2 fechas
from datetime import  date

hoy = date(2022, 4,26)

otra_fecha =date(2022, 4,26)

delta =otra_fecha - hoy

print(delta.days)