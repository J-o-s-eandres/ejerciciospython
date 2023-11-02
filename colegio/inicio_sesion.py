from tkinter import *
import mysql.connector
from tkinter import messagebox

def  INICIO():
    reg1=usuario.get()
    reg2=tpass.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="colegio")
    cur=conn.cursor()
    bus=int(reg1)
    cur.execute("select * from where dni={0}".format(bus))
    conn.commit()
    
def SALIR():
    menu.destroy()

usuario=StringVar
tpass=StringVar


menu=Tk()
menu.title("INICIAR SESION")
#menu.geometry("900x600")
positionRight = int(-10)
positionDown = int(0)
menu.geometry("+{}+{}".format(positionRight, positionDown))
menu.geometry("330x370")
menu.resizable(width=0,height=0)
Label(menu,text="I.E. THE BIG BANG NASA").place(x=90,y=5)

Label(menu,text="USUARIO").place(x=30,y=30)
Entry(menu,width=45,textvariable=usuario).place(x=30,y=50)

Label(menu,text="CONTRASEÑA").place(x=30,y=80)
Entry(menu,width=45,textvariable=tpass).place(x=30,y=100)

Button(menu,text="INICIAR",bg='green',width=35,command=INICIO).place(x=36,y=150)
Button(menu,text="SALIR",width=35,bg='red',command=SALIR).place(x=36,y=200)

menu.mainloop()