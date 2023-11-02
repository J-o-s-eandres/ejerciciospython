 #Vamos a crear nuestra propia metaclase

 #Creamos una clase que desciende de type
class MiMeta(type):

    #__new__ se ejecuta antesque __init__
    #Nos sirve para indicar como deseamos que se lleve a cabo la construccion del objeto
    # Como parametros obtenemos el nombre de la clase
    #Su clase base y los atributos
    #al final invocamos el constructor de type y regreamoslo que nos regrese

    def __new__(self, class_name, bases, attrs):
        print('Nombre: ', class_name)
        print('Base: ', bases)
        print('Atributos: ', attrs)

        #creamos un atributo propio
        #hacemos nuestro diccionario 
        d={}
        for elemento,valor in attrs.items():
            d[elemento]=valor

        d['miAtributo']='22'

        # return type(class_name, bases, attrs)
        return type(class_name, bases, d)

class miClase(metaclass=MiMeta):
    a=5
    nombre='joseandres'

    def imprime(self):
        print(self.nombre*self.a)
        print(self.miAtributo)

objeto1 = miClase()
objeto1.imprime()
objeto1.miAtributo