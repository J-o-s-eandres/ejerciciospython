#solicitar el valor del radio de un circulo para calcular el area

from math import pi
r = float(input("Escriba el radio el circulo: "))
area= pi * r**2

print("El area de un circulo que tiene un radio de {} es = {}".format(r,area))