# Los métodos mágicos también conocidos como dunder nos permite colocar
# a nuestras clases funcionalidades de alto nivel.

# Creamos una clase

class Producto:

    def __init__(self, nombre):
        self.nombre = nombre
    
    
    #1 __repr__ es usadi para realizar la impresion del objeto.
    def __repr__(self):
        return "El producto es: " + self.nombre


    #2 __mul__ es usado para decir como se lleva a cabo la multiplicación para unobjeto en nuestra clase

    def __mul__(self, operando):
        # Verificamos que el operando sea del tipo correcto
        if type(operando) is int:
            for n in range(operando):
                print(self.nombre)
                self.nombre= self.nombre*operando
        else:
            raise ValueError("Operando no válido")



# algunas clases se imprimen bien y en otras solo vemos la locación en memoria
miLista =[10,20,30,40]
print(miLista)


miLista2 = miLista*5
print(miLista2)

fruta= Producto('Mango')
print(fruta)

fruta*3
print(fruta)