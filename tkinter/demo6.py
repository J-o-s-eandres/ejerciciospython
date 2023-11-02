# **********************************************************************************
# Construir una aplicación, que solicite tu año de nacimiento y te devuelva tu edad
# Año naciste = 2000, el sistema devuelve = 21 (botones, cajas de texto)
# **********************************************************************************

# Importar la biblioteca (conjunto de librerías)
import tkinter

# Construir la ventana
ventana = tkinter.Tk()

# Personalizando nuestra ventana
ventana.title("Aprendiendo Tkinter")
ventana.geometry("500x300")

# Zona de funciones
def calcularEdad(aNacimiento):
    edad = 2021 - aNacimiento
    txtEdad.delete(0, tkinter.END)
    txtEdad.insert(0, str(edad))

# Fin de las funciones
lblAnac = tkinter.Label(ventana, text = "Año de nacimiento", font = "Arial 12")
lblEdad = tkinter.Label(ventana, text = "Ud. tiene", font = "Arial 12")
txtAnac = tkinter.Entry(ventana, font = "Arial 12")
txtEdad = tkinter.Entry(ventana, font = "Arial 12")
btnCalcular = tkinter.Button(ventana, text = "Calcular edad", font = "Arial 12", command = lambda:calcularEdad(int(txtAnac.get())))

lblAnac.place(x = 10, y = 10)
lblEdad.place(x = 10, y = 70)
txtAnac.place(x = 150, y = 10)
txtEdad.place(x = 150, y = 70)
btnCalcular.place(x = 150, y = 140)

# Mostrar la ventana y sus componentes (internos)
ventana.mainloop()