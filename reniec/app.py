import tkinter
from tkinter import messagebox as mb
import requests
import json

ventana = tkinter.Tk()
ventana.title("Consulta Reniec")

frm=tkinter.Frame(ventana)
frm.grid(column=0,row=0,padx=(25,25))

#consulta DNI

label1 = tkinter.Label(frm, text="Consulta de DNI",font="-weight bold")
label1.grid(row=0,column=0,pady=10)

anchoText= 35
#Txt BucarDNI
txtDNIBuscar=tkinter.Entry(frm,width=anchoText)
txtDNIBuscar.grid(row=1,column=0)

#Btn Buscar
btnBuscar= tkinter.Button(frm,text="Buscar",width=23,bg="green",fg="white",command=lambda: buscar())
btnBuscar.grid(row=2,column=0)


#response 
fila = 3

#DNI - CUI

label2= tkinter.Label(frm,text="DNI - CUI:")
label2.grid(row=fila,column=0, sticky="w")
fila = fila +1

txtDNICui= tkinter.Entry(frm,width=anchoText)
txtDNICui.grid(row=fila,column=0, sticky="w")
fila = fila +1

# PATERNO

label2= tkinter.Label(frm,text="A. Paterno:")
label2.grid(row=fila,column=0, sticky="w")
fila = fila +1

txtPaterno= tkinter.Entry(frm,width=anchoText)
txtPaterno.grid(row=fila,column=0, sticky="w")
fila = fila +1


# MATERNO

label2= tkinter.Label(frm,text="A. Materno:")
label2.grid(row=fila,column=0, sticky="w")
fila = fila +1

txtMaterno= tkinter.Entry(frm,width=anchoText)
txtMaterno.grid(row=fila,column=0, sticky="w")
fila = fila +1


# MATERNO

label2= tkinter.Label(frm,text="Nombres:")
label2.grid(row=fila,column=0, sticky="w")
fila = fila +1

txtNombres= tkinter.Entry(frm,width=anchoText)
txtNombres.grid(row=fila,column=0, sticky="w")
fila = fila +1

# SEXO

label2= tkinter.Label(frm,text="SEXO:")
label2.grid(row=fila,column=0, sticky="w")
fila = fila +1

txtSexo= tkinter.Entry(frm,width=anchoText)
txtSexo.grid(row=fila,column=0, sticky="w",pady=(0,10))
fila = fila +1
#fin del response

def buscar():
    dni= txtDNIBuscar.get()#obtener el valor del DNI

    txtPaterno.delete(0,tkinter.END)
    txtMaterno.delete(0,tkinter.END)
    txtNombres.delete(0,tkinter.END)
    txtDNICui.delete(0,tkinter.END)
    txtSexo.delete(0,tkinter.END)



    url = "https://www.softwarelion.xyz/api/reniec/reniec-dni"
    _json={"dni":dni}
    token ="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoyNDcxLCJjb3JyZW8iOiJqb3NlYW5kcmVzbW9udGVzaW5vQGdtYWlsLmNvbSIsImlhdCI6MTY2MjE0NzAzN30.pWb5tVxNtulWrYsep9Z8wv6shxaoAZFNRpKFSoTqkrA"
    _headers={"Content-Type":"application/json", "Authorization" : token }


    response = requests.post(url, data=json.dumps(_json),headers=_headers)
    dataJson= response.json()

    if (dataJson["success"] == False):
        mb.showwarning("Error",dataJson["message"])
        return

    persona = dataJson["result"]

    txtPaterno.insert(0,persona["paterno"])
    txtMaterno.insert(0,persona["materno"])
    txtNombres.insert(0,persona["nombres"])
    txtDNICui.insert(0,dni +"-"+ persona["codigoVerificacion"])
    txtSexo.insert(0,persona["Sexo"])





ventana.mainloop()