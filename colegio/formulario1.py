from tkinter import *
from tkinter import ttk
import mysql.connector

valu=Tk()
valu.geometry("650x500")
valu.title("Mantenimiento de Alumnos")
#valu.config(bg='white')
valu.resizable(width=0,height=0)

def guardar():
    dni=txtdni.get()
    nombre=txtnombre.get()
    apellido=txtapellido.get()
    edad=txtedad.get()
    celular=txtcelular.get
    conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="colegio")
    cur=conn.cursor()
    registro="insert into alumnos (dni,nombre,apellido,edad,telefono)\
    values ('{0}','{1}','{2}','{3}','{4}')".format(dni,nombre,apellido,edad,celular)
    cur.execute(registro)
    conn.commit()
    


txtdni=StringVar()
txtnombre=StringVar()
txtapellido=StringVar()
txtedad=StringVar()
txtcelular=StringVar()

Label(valu,text="DNI").place(x=30,y=30)
Entry(valu,width=45,textvariable=txtdni).place(x=130,y=30)
Label(valu,text="NOMBRE").place(x=30,y=60)
Entry(valu,width=45,textvariable=txtnombre).place(x=130,y=60)
Label(valu,text="APELLIDO").place(x=30,y=90)
Entry(valu,width=45,textvariable=txtapellido).place(x=130,y=90)
Label(valu,text="EDAD").place(x=30,y=120)
Entry(valu,width=45,textvariable=txtedad).place(x=130,y=120)
Label(valu,text="N° CELULAR").place(x=30,y=150)
Entry(valu,width=45,textvariable=txtcelular).place(x=130,y=150)

Button(valu,text="GUARDAR",width=15,bg='green',command=guardar).place(x=420,y=30)
Button(valu,text="ACTUALIZAR",width=15,bg='blue',).place(x=420,y=60)
Button(valu,text="ELIMINAR",width=15,bg='red',).place(x=420,y=90)
Button(valu,text="LIMPIAR",width=15,bg='purple',).place(x=420,y=120)

tree=ttk.Treeview(valu,selectmode="browse")
vsb=ttk.Scrollbar(orient="vertical",comman=tree.yview)
tree.configure(yscrollcommand=vsb.set)
tree.place(x=90,y=180)
tree['columns']=("1","2","3","4","5")
tree['show']="headings"
tree.column("1",width=65)
tree.heading("1",text="DNI")
tree.column("2",width=95)
tree.heading("2",text="NOMBRES")
tree.column("3",width=95)
tree.heading("3",text="APELLIDO")
tree.column("4",width=45)
tree.heading("4",text="EDAD")
tree.column("5",width=85)
tree.heading("5",text="N° CELULAR")

conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="colegio")
cur=conn.cursor()
cur.execute("select * from alumnos")
fila=cur.fetchall()
num=0

for fila in fila:
    tree.insert("",'end',text="Uno",values=(fila[0],fila[1],fila[2],fila[3],fila[4]))
num=+1
valu.mainloop()