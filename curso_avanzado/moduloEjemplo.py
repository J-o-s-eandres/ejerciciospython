"""modulo de ejemplo para el inspect

Keyword arguments:
argument -- modulo de ejemplo
Return: return ejemplos
"""

def miFuncion(parametro1, parametro2 = 'unTexto'):
    """ Esta es una función"""
    valor = parametro1 * 3
    print('hola'+ parametro2)
    return valor

class claseBase(object):
    """Ejemplo de clase"""

    def __init__(self,nombre):
        self.nombre = nombre

    def getNombre(self):
        #regresamos el nombre de la instancia
        return self.nombre

objeto1 = claseBase('primer objeto')

class claseHija(claseBase):
    """Clase hija"""
 

    #metodo de hija 

    def miMetodo(self):
        #aqui hacemos algo
        x=5

    def getNombre(self):
        #hacemos override
        return 'Clase Hija' + self.nombre