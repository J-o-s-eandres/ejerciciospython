from tkinter import *
from PIL import ImageTk, Image
#JOSEANDRES MONTESINO
#DEFINIMOS LAS FUNCIONES A UTILIZARSE
def vista():
    import  ferre_vista_inventario.py
def INICIO():
    import ferre_inicio_sesion.py
def SALIR():
    menu.destroy()
menu=Tk()
menu.title("Menu Principal")
positionRight = int(-10)
positionDown = int(0)
menu.geometry("+{}+{}".format(positionRight, positionDown))
menu.geometry("300x400")
menu.resizable(width=0,height=0)
frame=Frame(menu)
frame.place(x=0,y=0)
frame.config(width=300, height=650, )
Label(menu,text="FERRETERIA 'EL TORNILLO FELIZ'").place(x=60,y=10)
img=ImageTk.PhotoImage(Image.open("img/herramienta-de-llave.png"))
Label(menu,image=img).place(x=110,y=70)
img2=ImageTk.PhotoImage(Image.open("img/martillo.png"))
Label(menu,image=img2).place(x=115,y=300)

#BOTONES 
Button(menu,text="VER INVENTARIO ACTUAL",width=35,bg="#5065A1",command=vista).place(x=30,y=180)
Button(menu,text="INICIAR SESION",bg='green',command=INICIO,width=35).place(x=30,y=210)
Button(menu,text="CERRAR",width=35,bg='red',command=SALIR).place(x=30,y=240)

menu.mainloop()