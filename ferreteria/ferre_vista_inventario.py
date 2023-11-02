from tkinter import *
from tkinter import ttk
import mysql.connector
#JOSEANDRES MONTESINO
valu=Tk()
valu.geometry("650x450")
valu.title("VISTA ACTUAL DEL INVENTARIO")
#valu.config(bg='white')
valu.resizable(width=0,height=0)
frame=Frame(valu)
frame.place(x=0,y=0)
frame.config(width=650, height=450, bg="#5065A3")

Label(valu,text="FERRETERIA 'EL TORNILLO FELIZ'").place(x=235,y=30)
Label(valu,text="INVENTARIO ACTUAL").place(x=265,y=80)

tree=ttk.Treeview(valu,selectmode="browse")
vsb=ttk.Scrollbar(orient="vertical",comman=tree.yview)
tree.configure(yscrollcommand=vsb.set)
tree.place(x=90,y=120)
tree['columns']=("1","2","3","4","5")
tree['show']="headings"
tree.column("1",width=87)
tree.heading("1",text="CODIGO")
tree.column("2",width=112)
tree.heading("2",text="NOMBRES")
tree.column("3",width=97)
tree.heading("3",text="MEDIDA")
tree.column("4",width=87)
tree.heading("4",text="PRECIO")
tree.column("5",width=87)
tree.heading("5",text="STOCK")
conn=mysql.connector.connect(host="localhost",user="root",passwd="",database="herramientas")
cur=conn.cursor()
cur.execute("select * from productos")
fila=cur.fetchall()
num=0
for fila in fila:
    tree.insert("",'end',text="Uno",values=(fila[0],fila[1],fila[2],fila[3],fila[4]))
num=+1
valu.mainloop()