import tkinter

ventana = tkinter.Tk()

ventana.title("Trabajando con botones")
ventana.geometry("600x400")

# Funciones (acción/acciones) que puede realizar el botón
def mostrarSaludo():
    print("Hola mundo")
    etiqueta1["text"] = "Hola mundo"

# Botón
etiqueta1 = tkinter.Label(ventana, text = "Mensaje...", font = "Impact 24", bg = "red", fg = "white")
boton1 = tkinter.Button(ventana, text = "Pulsa este botón", font = "Arial 16", command = mostrarSaludo)

boton1.pack()
etiqueta1.place(x = 200, y = 150)

ventana.mainloop()