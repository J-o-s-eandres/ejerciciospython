# **kwargs crea un diccionario 
'''
def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave}: {valor}')

listarTerminos(IDE ='Integrated Development Environment', OOP='Object Oriented Programming',DBMS ='Database Management System')      

'''

"""
def desplegarNombres(nombres):
    for nombre in nombres: 
        print(nombre)

nombres = ['Juan', 'Pedro', 'Joseandres']

desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((8,9,1,2,3,4,5))
desplegarNombres([1,2,3,4,5])

"""

'''
#funcion para calcular impuestos
def calcularImpuesto(pago,impuesto):
    pagoTotal= pago + pago *(impuesto/100)
    return pagoTotal


pago= float(input("Ignrese el pago sin impuesto: "))
impuesto= float(input("Ingrese el monto del impuesto a aplicar: "))

pagoImpuesto= calcularImpuesto(pago,impuesto)

print(f'Pago con impuesto: {pagoImpuesto}')

'''

#funciones para convertir temperatura

# funcion que convierte de celsius a fahrenheit


def funcelsius(celsius):
    return celsius * 9 / 5 +32

#funcion que convierte de fahrenheit a celsius
def funfahrenheit(fahrenheit):
    return(fahrenheit - 32) * 5 / 9

#pruebas de conversion

celsius= float(input("Ingrese su valor en celsius: "))

resultado = funcelsius(celsius)
print(f'{celsius} C a F: {resultado:.2f} ')#:.2F es para la cantidad de flotantes


fahrenheit = float(input("Ingrese su valor en fahrenheit: "))

resultado = funfahrenheit(fahrenheit)

print(f'{fahrenheit} F a C {resultado:0.2f}')
