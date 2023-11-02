#es un bloque de codigo que podemos llamar n cantidad de veces
'''
def mi_funcion():
    print("holis desde la funcion")

mi_funcion()

'''
#funcion con argumentos los valores que enviamos a la funcion /parametros= variables que declaremos dentro de la funcion
'''
def mi_funcion(nombre, apellido):
    print("holis desde la funcion")
    print(f'Nombre: {nombre}, Apellido: {apellido}')

mi_funcion('Joseandres', 'Montesino')

'''
'''
def suma(num1:int,num2:int):
    return num1 + num2

#resultado= suma(1,2)
#print(f'resultado suma: {resultado}')
print(f'Resultado suma: {suma(1,2)}')
'''


#def sumar(a:int = 0, b : int = 0)-> int :#valores por default e indicamos una pista de que retornara un numero entero (python es dinamico asi que igual puede retornar lo qeu ele mandes ) se considera hacer esto redundante
'''
def sumar(a = 0, b = 0):
    return a + b

print(f'Resultado suma: {sumar(5,5)}')
'''

#argumentos variables *args 


def listarNombres(*nombres):#con *nombre creamos una tupla y por eso podemos recorrer
    for nombre in nombres:
        print(nombre)

listarNombres('juan','pedro','jose','pepe')