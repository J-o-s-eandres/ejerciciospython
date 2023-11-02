import tkinter
ventana = tkinter.Tk()
ventana.title("Trabajando con etiquetas")
ventana.geometry("500x500")
ventana.resizable(True, True)

# Construir 4 etiquetas
# Arial, Impact, Calibri, Impact
etiqueta1 = tkinter.Label(ventana, text = "Python", font = "Impact 30", bg = "red", fg = "yellow")
etiqueta2 = tkinter.Label(ventana, text = "Javascript", font = "Tahoma 12", bg = "#000", fg = "#FFF")
etiqueta3 = tkinter.Label(ventana, text = "Java", font = "Arial 18")
etiqueta4 = tkinter.Label(ventana, text = "SQL", font = "Verdana 24")

# Añadiendo etiquetas
etiqueta1.pack(side = tkinter.LEFT)
etiqueta2.pack(side = tkinter.RIGHT)
etiqueta3.pack(side = tkinter.TOP)
etiqueta4.pack(side = tkinter.BOTTOM)

ventana.mainloop()