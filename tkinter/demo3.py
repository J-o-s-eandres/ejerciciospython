import tkinter

ventana = tkinter.Tk()
ventana.title("Moviendo elementos")
ventana.geometry("600x400")     # AnchoxAlto

etiqueta1 = tkinter.Label(ventana, text = "MySQL", font = "Arial 18")
etiqueta2 = tkinter.Label(ventana, text = "Microsoft SQL Server", font = "Arial 18")
etiqueta3 = tkinter.Label(ventana, text = "Oracle Database", font = "Arial 18")

# El método pack() permite agregar el widget(componente/Label) al formulario
# en una posición (lado) indicada 
# etiqueta1.pack()
# etiqueta2.pack()
# etiqueta3.pack()

etiqueta1.place(x = 250, y = 180)
etiqueta2.place(x = 0, y = 0)
etiqueta3.place(x = 400, y = 250)

ventana.mainloop()