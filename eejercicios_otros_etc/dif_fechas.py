#Calcular la diferencia en dias de las fechas dadas

from datetime import date

anio_actual=int(input("ingrese el año actual: "))
mes_actual=int(input("ingrese el mes actual: "))
dia_actual=int(input("ingrese el dia actual: "))

hoy =date(anio_actual,mes_actual,dia_actual)

print("La fecha ingresada es: " + str(hoy))

anio_viejo=int(input("ingrese un año: "))
mes_viejo=int(input("ingrese un mes: "))
dia_viejo=int(input("ingrese un dia: "))

fecha_pasada= date(anio_viejo, mes_viejo, dia_viejo)

print("La fecha ingresada es: " + str(fecha_pasada))

diferencia=hoy - fecha_pasada

print()
print('entre {} y {} hay {} dias de diferencia'.format(fecha_pasada,hoy,diferencia.days))


