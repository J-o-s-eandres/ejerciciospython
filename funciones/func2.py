"""
Crear una funcion para sumar los valores recibidos de tipo numerico,
utilizando argumentos variables *args como parametro de la funcion y
regresar como resultado la suma de todos los valores pasados como argumentos.
"""

#definimos nuestra funcion parasumar valores
'''
def sumar_valores(*args):
    resultado=0
    #iteramos cada elemento
    for i in args:
        resultado += i
        #resultado = resultado + i
    return resultado

#llamada de la funcion
print(sumar_valores(3,5,6,7,8,8,7,6,5,5,3,3,2,2))
'''


def multiplicar_valores(*args):
    resultado = 1
    for i in args:
        resultado *= i
    return resultado

print( multiplicar_valores(1,2,3))