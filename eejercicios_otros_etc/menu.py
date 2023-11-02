from tkinter import *
from PIL import ImageTk, Image
from matplotlib.pyplot import text



def REGISTRARSE():
    import registro_alumno.py
def INICIO():
    import inicio_sesion.py

def SALIR():
    menu.destroy()

menu=Tk()
menu.title("Menu Principal")
#menu.geometry("900x600")
positionRight = int(-10)
positionDown = int(0)
menu.geometry("+{}+{}".format(positionRight, positionDown))
menu.geometry("300x400")
menu.resizable(width=0,height=0)
frame=Frame(menu)
frame.place(x=0,y=0)
frame.config(width=300, height=650, bg="#5065A3")
Label(menu,text="I.E. THE BIG BANG NASA").place(x=90,y=10)
img=ImageTk.PhotoImage(Image.open("img/educacion.png"))
Label(menu,image=img).place(x=90,y=40)

Button(menu,text="REGISTRARSE",width=35,command=REGISTRARSE).place(x=30,y=180)
Button(menu,text="INICIAR SESION",bg='green',command=INICIO,width=35).place(x=30,y=210)
Button(menu,text="CERRAR",width=35,bg='red',command=SALIR).place(x=30,y=240)

menu.mainloop()

