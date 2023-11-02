from tkinter import *
from tkinter import messagebox
import mysql.connector


menu=Tk()
menu.title("REGISTRO DE PRODUCTOS")
#menu.geometry("900x600")
positionRight = int(-10)
positionDown = int(0)
menu.geometry("+{}+{}".format(positionRight, positionDown))
menu.geometry("350x500")
menu.resizable(width=0,height=0)
Label(menu,text="FERRETERIA 'EL TORNILLO FELIZ'").place(x=90,y=5)


def  REGISTRARSE():
    dcodigo=codigo.get()
    dnombre=nombre.get()
    dmedida=medida.get()
    dprecio=precio.get()
    dstock=stock.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="herramientas")
    cur=conn.cursor()
    registro="insert into productos (codigo_product,nombre_product,medida,precio,stock)\
    values ('{0}','{1}','{2}','{3}','{4}')".format(dcodigo,dnombre,dmedida,dprecio,dstock)
    messagebox.showinfo("NOTIFICACION","EL PRODUCTO {} A SIDO INSERTADO CORRECTAMENTE CON EL CODIGO {}".format(dnombre,dcodigo))
    cur.execute(registro)
    conn.commit()
    
    

def SALIR():
    menu.destroy()


codigo=StringVar()
nombre=StringVar()
medida=StringVar()
precio=StringVar()
stock=StringVar()

Label(menu,text="CODIGO",).place(x=30,y=30)
Entry(menu,width=45,textvariable=codigo).place(x=30,y=50)

Label(menu,text="NOMBRE",).place(x=30,y=80)
Entry(menu,width=45,textvariable=nombre).place(x=30,y=100)

Label(menu,text="MEDIDA").place(x=30,y=130)
Entry(menu,width=45,textvariable=medida).place(x=30,y=150)

Label(menu,text="PRECIO").place(x=30,y=180)
Entry(menu,width=45,textvariable=precio).place(x=30,y=200)

Label(menu,text="STOCK").place(x=30,y=230)
Entry(menu,width=45,textvariable=stock).place(x=30,y=250)




Button(menu,text="AGREGAR AL INVENTARIO",bg='green',width=35,command=REGISTRARSE).place(x=36,y=350)
Button(menu,text="SALIR",width=35,bg='red',command=SALIR).place(x=36,y=400)

menu.mainloop()