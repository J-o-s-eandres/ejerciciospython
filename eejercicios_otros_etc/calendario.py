#imprimir el calendario para un año y mes especifico
import calendar

anio= int(input('Escriba el año: '))
mes= int(input('Escriba el mes: '))

print(calendar.month(anio, mes))