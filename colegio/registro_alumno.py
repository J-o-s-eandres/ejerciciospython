from tkinter import *
from tkinter import messagebox
import mysql.connector


menu=Tk()
menu.title("REGISTRO DE ALUMNOS")
#menu.geometry("900x600")
positionRight = int(-10)
positionDown = int(0)
menu.geometry("+{}+{}".format(positionRight, positionDown))
menu.geometry("350x500")
menu.resizable(width=0,height=0)
Label(menu,text="I.E. THE BIG BANG NASA").place(x=90,y=5)

def  REGISTRARSE():
    dni=txtdni.get()
    nombre=txtnombre.get()
    apellido=txtapellido.get()
    edad=txtedad.get()
    password=txtpass.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="colegio")
    cur=conn.cursor()
    registro="insert into alumnos (dni,nombre,apellido,edad,password)\
    values ('{0}','{1}','{2}','{3}','{4}')".format(dni,nombre,apellido,edad,password)
    messagebox.showinfo("NOTIFICACION","EL ALUMNO FUE AGREGADO CORRECTAMENTE")
    cur.execute(registro)
    conn.commit()
    
    

def SALIR():
    menu.destroy()


txtdni=StringVar()
txtnombre=StringVar()
txtapellido=StringVar()
txtedad=StringVar()
txtpass=StringVar()

Label(menu,text="DNI",).place(x=30,y=30)
Entry(menu,width=45,textvariable=txtdni).place(x=30,y=50)

Label(menu,text="NOMBRE",).place(x=30,y=80)
Entry(menu,width=45,textvariable=txtnombre).place(x=30,y=100)

Label(menu,text="APELLIDO").place(x=30,y=130)
Entry(menu,width=45,textvariable=txtapellido).place(x=30,y=150)

Label(menu,text="EDAD").place(x=30,y=180)
Entry(menu,width=45,textvariable=txtedad).place(x=30,y=200)

Label(menu,text="PASSWORD").place(x=30,y=230)
Entry(menu,width=45,textvariable=txtpass).place(x=30,y=250)




Button(menu,text="REGISTRARSE",bg='green',width=35,command=REGISTRARSE).place(x=36,y=350)
Button(menu,text="SALIR",width=35,bg='red',command=SALIR).place(x=36,y=400)

menu.mainloop()