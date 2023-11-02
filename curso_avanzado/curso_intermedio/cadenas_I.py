#strip elimina el exceso de espacios vacios

mensaje="   hola a todos  "
mCorto = mensaje.strip()

print('----'+mensaje+'---')
print('----'+mCorto+'---')

print('----'+mensaje.lstrip()+'---')
print('----'+mensaje.rstrip()+'---')


#len nos da la cantidad de caracteres

nombre = 'Joseandres'
n = len(nombre)

print(nombre, 'tiene ', n , ' caracteres')


#lower cambia todas las letras a minusculas
texto ='Hola gente'
minusculas = texto.lower()
print(minusculas)

#upper cambia todas las letras a mayusculas
mayusculas = texto.upper()
print(mayusculas)


#split crea una lista a partir de la cadena , dbeemoscolocar el delimitador que indica donde hacer los cortes

palabras = texto.split(' ')
print(palabras)


valores = '5,6,7,8,9,11,14'
datos = valores.split(',')
print(datos)