# Importar la biblioteca (conjunto de librerías)
import tkinter

# Construir la ventana
ventana = tkinter.Tk()

# Personalizando nuestra ventana
ventana.title("Aprendiendo Tkinter")
ventana.geometry("500x300")

# Crear diccionario (esto es un ejemplo, los valores numéricos NO REPRESENTAN NADA IMPORTANTE)
sistemasOperativos = {
    "Windows 10"        : 150,
    "Linux Ubuntu 21"   : 0,
    "Android 11"        : 10,
    "iOS"               : 50
}

# Funciones
def describeLP(nombre):
    if nombre == "Python":
        print("Es una magnífico LP, muy fácil de utilizar")
    elif nombre == "C#":
        print("Es un lenguaje muy potente desarrollado por Microsoft")
    elif nombre == "Java":
        print("LP muy versátil porque lo podemos utilizar para todo")
    else:
        print("Completar para los otros lenguajes")

def describeSO(nombre):
    print(sistemasOperativos[nombre])

# Fin de las funciones

# Elemento donde desplegamos las opciones
listaLP = tkinter.StringVar(ventana, value = "Seleccione un lenguaje") 
listaSO = tkinter.StringVar(ventana, value = "Elige un sistema operativo")

# Tupla = colección de elementos inmutables (no va a cambiar)
misLenguajes = ("Python", "C#", "Java", "Javascript", "C++")
misSO = ("Windows 10", "Linux Ubuntu 21", "Android 11", "iOS")

# Este control, será el que agregamos a la ventana
controlListaLP = tkinter.OptionMenu(ventana, listaLP, *misLenguajes, command = describeLP)
controlListaSO = tkinter.OptionMenu(ventana, listaSO, *misSO, command = describeSO)

controlListaLP.grid(row = 0, column = 0)
controlListaSO.grid(row = 0, column = 1)

ventana.mainloop()