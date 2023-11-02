import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import prueba2

class FormularioPrueba:
    def __init__(self):
        self.prueba1=prueba2.Conector()
        self.ventana1=tk.Tk()
        self.ventana1.title("Prueba")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        self.consulta_por_dni()
        self.agregar_alumno()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

#VENTANA DE AGREGAR ALUMNOS

    def agregar_alumno(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="AGREGAR ALUMNOS")
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="DATOS DE ALUMNO")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe1, text="DNI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.dnicarga=tk.StringVar()
        self.entrydni=ttk.Entry(self.labelframe1, textvariable=self.dnicarga)
        self.entrydni.grid(column=1, row=0, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def agregar(self):
        datos=(self.dnicarga.get())
        self.prueba1.agregar_alumno(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.dnicarga.set("")

#VENTANA DE CONSULTAR       

    def consulta_por_dni(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="CONSULTA POR DNI")
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="DATOS")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="DNI:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.dni=tk.StringVar()
        self.entrydni=ttk.Entry(self.labelframe2, textvariable=self.dni)
        self.entrydni.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="NOMBRE:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)


    def consultar(self):
        datos=(self.dni.get(), )
        respuesta=self.prueba1.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][0])
        else:
            self.nombre.set('')
            mb.showinfo("Información", "No existe un alumno con dicho dni")        

aplicacion1=FormularioPrueba()
