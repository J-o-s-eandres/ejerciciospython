import pywhatkit

tlf= input('Ingrese el numero de telefono: ')
mensaje= input('ingrese el mensaje: ')

pywhatkit.sendwhatmsg(tlf,mensaje,16,14)
