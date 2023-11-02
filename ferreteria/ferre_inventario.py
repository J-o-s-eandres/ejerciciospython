from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox

valu=Tk()
valu.geometry("650x500")
valu.title("PANEL PRINCIPAL DE INVENTARIO")
#valu.config(bg='white')
valu.resizable(width=0,height=0)

def guardar():
    dcodigo=codigo.get()
    dnombre=nombre.get()
    dmedida=medida.get()
    dprecio=precio.get()
    dstock=stock.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="herramientas")
    cur=conn.cursor()
    registro="insert into productos (codigo_product,nombre_product,medida,precio,stock)\
    values ('{0}','{1}','{2}','{3}','{4}')".format(dcodigo,dnombre,dmedida,dprecio,dstock)
    messagebox.showinfo("NOTIFICACION","EL PRODUCTO {} A SIDO GUARDADO CORRECTAMENTE CON EL CODIGO {}".format(dnombre,dcodigo))
    limpiar()
    cur.execute(registro)
    conn.commit()

def eliminar():
    dcodigo=codigo.get()
    dnombre=nombre.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="herramientas")
    cur=conn.cursor()
    registro="select *from alumnos where (codigo_product,nombre_product)\
    values ('{0}','{1}')".format(dcodigo,dnombre)
    messagebox.showinfo("NOTIFICACION","EL PRODUCTO {} A SIDO ELIMINADO CORRECTAMENTE  ".format(dnombre))
    limpiar()
    cur.execute(registro)
    conn.commit()   
def salir():
    valu.destroy()

def actualizar():
    dcodigo=codigo.get()
    dnombre=nombre.get()
    dmedida=medida.get()
    dprecio=precio.get()
    dstock=stock.get()
    conn=mysql.connector.connect(host="localhost",user="root",password="",database="herramientas")
    cur=conn.cursor()
    sql="UPDATE SET codigo_product='{0}',nombre='{1}',medida='{2}', precio='{3}' WHERE codigo_product='{4}'".format(dcodigo,dnombre,dmedida,dprecio,dstock)
    messagebox.showinfo("NOTIFICACION","EL PRODUCTO {} A SIDO ACTUALIZADO CORRECTAMENTE LA CANTIDAD EXISTENTE ES: {}".format(dnombre,dstock))
    limpiar()
    cur.execute(sql)
    conn.commit()
    conn.close()
    #joseandres montesino

def limpiar():
    codigo.set("")
    nombre.set("")
    medida.set("")
    precio.set("")
    stock.set("")

#joseandres montesino

codigo=StringVar()
nombre=StringVar()
medida=StringVar()
precio=StringVar()
stock=StringVar()

Label(valu,text="CODIGO").place(x=30,y=30)
ttk.Entry(valu,width=45,textvariable=codigo).place(x=130,y=30)
Label(valu,text="NOMBRE").place(x=30,y=60)
ttk.Entry(valu,width=45,textvariable=nombre).place(x=130,y=60)
Label(valu,text="MEDIDA").place(x=30,y=90)
ttk.Entry(valu,width=45,textvariable=medida).place(x=130,y=90)
Label(valu,text="PRECIO").place(x=30,y=120)
ttk.Entry(valu,width=45,textvariable=precio).place(x=130,y=120)
Label(valu,text="STOCK").place(x=30,y=150)
ttk.Entry(valu,width=45,textvariable=stock).place(x=130,y=150)

Button(valu,text="GUARDAR",width=15,bg='green',command=guardar).place(x=420,y=30)
Button(valu,text="ACTUALIZAR",width=15,bg='blue',command=actualizar).place(x=420,y=60)
Button(valu,text="ELIMINAR",width=15,bg='red',command=eliminar).place(x=420,y=90)
Button(valu,text="LIMPIAR",width=15,bg='purple',command=limpiar).place(x=420,y=120)
Button(valu,text="SALIR",width=15,bg='silver',command=salir).place(x=470,y=420)

tree=ttk.Treeview(valu,selectmode="browse")
vsb=ttk.Scrollbar(orient="vertical",comman=tree.yview)
tree.configure(yscrollcommand=vsb.set)
tree.place(x=90,y=180)
tree['columns']=("1","2","3","4","5")
tree['show']="headings"
tree.column("1",width=65)
tree.heading("1",text="CODIGO")
tree.column("2",width=95)
tree.heading("2",text="NOMBRES")
tree.column("3",width=95)
tree.heading("3",text="MEDIDA")
tree.column("4",width=45)
tree.heading("4",text="PRECIO")
tree.column("5",width=85)
tree.heading("5",text="STOCK")
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="herramientas")
cur=conn.cursor()
cur.execute("select * from productos")
fila=cur.fetchall()
num=0
#JOSEANDRES MONTESINO
for fila in fila:
    tree.insert("",'end',text="Uno",values=(fila[0],fila[1],fila[2],fila[3],fila[4]))
num=+1
valu.mainloop()