from distutils import command
from tkinter import *
#configuracion de venetana
ventana= Tk()
ventana.title('Juego de Azar')
ventana.config(background="#B1CFE2")
ventana.geometry("800x600")
#------------------------------------------------
def juego():
    cargar=num.get()#=obtenemos el valor de la caja
    if(cargar == ""):#si la caja esta vacia le asignamos el primer valor
        num.set(1)#se agg 1 como primer valor
    else:
      conteo=int(num.get())#en caso si tenga numero la caja sumar de 1 en 1 
      num.set(1+(conteo))
    
#declaracion de variables
num=StringVar()

#-------------------------------controles
Label(ventana,text="intento").place(x=10,y=10)
Entry(ventana,textvariable=num).place(x=10,y=40)
Button(ventana,text="JUGAR",command=juego).place(x=140,y=38.4)


ventana.mainloop()