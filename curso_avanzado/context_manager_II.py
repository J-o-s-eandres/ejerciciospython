#Hacemos una clase
class miMC:

    def __init__(self, archivo, abrir):
        self.archivo= open(archivo, abrir)

    # Este es el codigo de entrada
    def __enter__(self):
        print("En la entrada")
        #regresamos la referencia al archivo abierto
        return self.archivo

#Aquí colocamos el codigo de salida
#Si hay una excepcion se espera que aqui se maneje

    def __exit__(self, type, value, traceback):
        print("En la salida")

        #Obtenemos la informacion de la excepcion

        print('type------ : ',type)
        print('value ------ : ',value)
        print('tracebak ------ : ',traceback)

        self.archivo.close()

        #Si decidimos que esa excepcion no crea problemas
        #o ya lo manejamos correctamente regresamos true
        # Y ya no crashea el programa
        if type==ZeroDivisionError:
            #aqui manejamos la excepcion
            print('No dividir entre cero')
            return True

        if type == RuntimeError:
            print('Colocar la excepcion a levantar')
            return True

# Ponemos el context manager
# lo que regresa enter cae en archivo
with miMC('miArchivo.txt', 'w') as archivo:
    #aqui el codigo que deseamos que se ejecute
    print("En el context manager")
    archivo.write('Holiwis gentita')
    raise
    a=5/0
    #colocamos codigo que genere una excepcion