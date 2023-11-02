# Context manager nos garantiza que cierta operacion va a ocurrir
# en caso de que cierto fragmento truene o finalice la ejecución.


######## Aquí todo normal y bien 

a, b = 5, 0

archivo = open('miArchivo.txt', 'w')
archivo.write('hello gente')

#aqui podemos hacer una excepción que no nos permita llegar a close

# r=a/b
archivo.close()


##### Podemos solucionar las excepciones 

a, b= 5 , 3

archivo=open('miArchivo.txt', 'w')

try:
    archivo.write('hola gente')

    r=a/b

finally:
    archivo.close()

### Ahora veamos la sulición con context manager

#hacemos una clase

class miCM:
    def __init__(self,archivo, abrir):
        self.archivo=open(archivo, abrir)

    #este es el código de entrada
    def __enter__(self):
        print("En la entrada")
        #regresamos la referencia al archivo abierto
        return self.archivo

    #Aqui colocamos el codigo de salida
    def __exit__(self, type, value, traceback):
        print("En la salida")
        self.archivo.close()

#Ponemos el context manager
#Lo que regresa enter cae en archivo

with miCM('miArchivo.txt', 'w') as archivo:
    #aqui el codigo que deseamos que se ejecute
    print("En el context manager")
    archivo.write("hello gente")
