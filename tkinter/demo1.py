# Importamos la biblioteca (conjunto de clases) tkinter
import tkinter

# Creamos la ventana (interfaz principal)
ventana = tkinter.Tk()

# Asignar un título
ventana.title("SENATI - Curso de Algoritmia")

# Asignación de color
# https://htmlcolorcodes.com/es/
ventana.config(background="#B1CFE2")

# Asignar un tamaño a la ventana
ventana.geometry("600x400")

# Añadir controles al formulario
# El primer paso es crear el elemento | Label = Etiqueta(texto)
etiqueta = tkinter.Label(ventana, text = "Hola mundo")
programador = tkinter.Label(ventana, text = "Jhon Francia Minaya")

# Luego lo agregamos al formulario ("ventana")
etiqueta.pack()
programador.pack()

# Ejecutar el programa (permite a la ventana mantenerse al frente)
ventana.mainloop()