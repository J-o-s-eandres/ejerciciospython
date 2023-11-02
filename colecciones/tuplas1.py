#no son mutaples
#si declaramos una tupla de 1 solo elemento debemos poner una coma al final del elemento (solo si es 1 elemento)
#ejemplo: frutas = ('Banana',) de lo contratio de almacena como un string y no como tupla

frutas = ('Banana','Naranja','platano','Manzana')

#saber largo de la tupla

print(len(frutas))
print(frutas)

#acceder a un elemento
print(frutas[0])
print(frutas[-1])

#revisar si un elemento esta presente 
print('Marte' in frutas)

#acceder a un rango de valores

print(frutas[ :2])

#recorrer una tupla
for fruta in frutas:
    print(fruta)



#cambiar valor de una tupla de forma indirecta convertir a lista y viceversa

frutaLista = list(frutas)

frutaLista[0] = 'Pera'

frutas = tuple(frutaLista)
print('\n',frutas)

#eliminar tupla
del frutas


