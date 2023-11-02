from tkinter import *
from tkinter import ttk

valu=Tk()
valu.geometry("1150x500")
valu.title("Mantenimiento de Alumnos")

Label(valu,text="DNI").place(x=30,y=30)
Entry(valu,width=45).place(x=130,y=30)
Label(valu,text="NOMBRE").place(x=30,y=60)
Entry(valu,width=45).place(x=130,y=60)
Label(valu,text="APELLIDO").place(x=30,y=90)
Entry(valu,width=45).place(x=130,y=90)
Label(valu,text="EDAD").place(x=30,y=120)
Entry(valu,width=45).place(x=130,y=120)
Label(valu,text="N° CELULAR").place(x=30,y=150)
Entry(valu,width=45).place(x=130,y=150)

Button(valu,text="GUARDAR",width=15).place(x=420,y=30)

tree=ttk.Treeview(valu,selectmode="browse")
vsb=ttk.Scrollbar(orient="vertical",comman=tree.yview)
tree.configure(yscrollcommand=vsb.set)
tree.place(x=30,y=180)
tree['columns']=("1","2","3","4","5")
tree['show']="headings"
tree.heading("1",text="DNI")
tree.heading("2",text="NOMBRES")
tree.heading("3",text="APELLIDO")
tree.heading("4",text="EDAD")
tree.heading("5",text="N° CELULAR")
valu.mainloop()