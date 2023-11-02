from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import random

#las funciones
def juego():
    cargar=num.get()
    if(cargar==""):
        num.set(1)
        ale1=random.randint(1,5)
        val1.set(ale1)
        ale2=random.randint(1,5)
        val2.set(ale2)
        ale3=random.randint(1,5)
        val2.set(ale3)
    else:
        conteo=int(num.get())
        num.set(1+conteo)
        ale1=random.randint(1,5)
        val1.set(ale1)
        ale2=random.randint(1,5)
        val2.set(ale2)
        ale3=random.randint(1,5)
        val3.set(ale3)


#creacion del formulario
game=Tk()
game.title("JUEGO DE AZAR")
game.geometry("400x300")
#declarar variables
num=StringVar()
val1=StringVar()
val2=StringVar()
val3=StringVar()
opc=StringVar()
#construcción de controles
Label(game,text="Intento").place(x=10,y=10)
Entry(game,textvariable=num,width=10).place(x=10,y=40)
Button(game,text="JUGAR",command=juego,background="#CC66FF",width=12).place(x=110,y=30)
Label(game,text="1er valor").place(x=10,y=100)
Entry(game,textvariable=val1,width=10).place(x=10,y=140)
Label(game,text="2do valor").place(x=110,y=100)
Entry(game,textvariable=val2,width=10).place(x=110,y=140)
Label(game,text="3er valor").place(x=220,y=100)
Entry(game,textvariable=val3,width=10).place(x=220,y=140)
Entry(game,textvariable=opc,width=40).place(x=40,y=190)

#imagen
img=ImageTk.PhotoImage(Image.open("logo.jpg"))
Label(game,image=img).place(x=220,y=10)
game.mainloop()