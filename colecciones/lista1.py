#son mutables 
nombres = ["Esbelia","Joseandres","Barbara","Seynet"]

print(nombres)

#acceder a los elementos 1x1 mediante indices
print(nombres[0])
print(nombres[-1])

#rangos
print(nombres[0:2])
#del inicio hasta el indice 3 (sin incluir el indice 3)
print(nombres[:3])
#desde el indice indicado hasta el final
print(nombres[0:])

#cambiar un valor 
nombres[3]='Gabriela'
print(nombres)# al imprimir vemos que el valor (Seynet) en el indice 3 fue cambiado por (Gabriela)

#iterar una lista
for nombre in nombres:
    print(nombre)

else:
    print('no existen mas nombres en la lista')

#revisar si un elemento esta presente 
print('Marte' in nombres)

#preguntar el largo de una lista (elementos de una lista)
print(len(nombres))

#agg un elemento 

nombres.append('Adriana')#se agg al final (seria indice 4 en este caso)
print(nombres)

#insentar un elemento en un Indice en especifico(los demas elemntos se mueven a la derecha(corren uno))
nombres.insert(1, 'Andrea')#agg "Andrea" al indice 1 ( los demas se mueven)
print(nombres)

#remover un elemento
nombres.remove('Andrea') #remueve por valor 
print(nombres)

#remover ultimo valor agg
nombres.pop() #tambien puede eliminar el indice que se le pase (pero por defecto(dejandola vacia elimina el ultimo valor en agregarse y si ese valor ya fue eliminado pasa al penultimo y asi sucesivamente))
print(nombres)

#eliminar elemento en un indice indicado
del nombres [0]
print(nombres)

#limpiar todos los elementos de la lista

nombres.clear()
print(nombres)

#eliminar lista

del nombres # no podemos acceder porque se elimina de la memoria 

