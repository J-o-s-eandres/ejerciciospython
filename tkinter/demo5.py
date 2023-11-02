# Importar la biblioteca (conjunto de librerías)
import tkinter

# Construir la ventana
ventana = tkinter.Tk()

# Personalizando nuestra ventana
ventana.title("Aprendiendo Tkinter")
ventana.geometry("600x150")

# Sección para FUNCIONES
def describeC1():
    txtIngSoft.delete(0, tkinter.END)                                   # Primero debemos eliminar cualquier contenido previo
    txtIngSoft.insert(0, "Es la carrera donde desarrollamos APP")       # Segundo, asignamos el valor a mostrar

def describeC2():
    txtDiseno.delete(0, tkinter.END)
    txtDiseno.insert(0, "Construimos hermosos contenidos")

def describeC3():
    txtSeguridad.delete(0, tkinter.END)
    txtSeguridad.insert(0, "Nos preocupamos por la seguridad de la empresa")

# Fin de las funciones

# Construyendo botones (x3)
btnIngSoft = tkinter.Button(ventana, text = "Ingeniería de Software", font = "Arial 12", command = describeC1)
btnDiseno = tkinter.Button(ventana, text = "Diseño Gráfico Digital", font = "Arial 12", command = describeC2)
btnSeguridad = tkinter.Button(ventana, text = "Seguridad Informática", font = "Arial 12", command = describeC3)

# Cajas de texto
txtIngSoft = tkinter.Entry(ventana, font = "Arial 12", width = 40)
txtDiseno = tkinter.Entry(ventana, font = "Arial 12" , width = 40)
txtSeguridad = tkinter.Entry(ventana, font = "Arial 12" , width = 40)

# Añadir componentes a la ventana
# btnIngSoft.pack(side = tkinter.RIGHT)
# btnIngSoft.place(x = 200, y = 150)
btnIngSoft.grid(row = 0, column = 0)
btnDiseno.grid(row = 1, column = 0)
btnSeguridad.grid(row = 2, column = 0)

txtIngSoft.grid(row = 0, column = 1)
txtDiseno.grid(row = 1, column = 1)
txtSeguridad.grid(row = 2, column = 1)

# Mostrar la ventana y sus componentes (internos)
ventana.mainloop()