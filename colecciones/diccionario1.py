#organizacion de diccionario (clave : valor) => (key:value) /no hay indices

diccionario = {
    'IDE' : 'Integrated Development Environment',
    'OOP' : 'Object Oriented Programming ',
    'DBMS': 'Database Management System'
}

print(diccionario)

#cantidad de elemento
print(len(diccionario))

#acceder a un elemento (mediante el key 'la llave')
print(diccionario['IDE'])
#otra forma de recuperar un elemento
print(diccionario.get('OOP'))

#modificar elementos
diccionario['IDE']= 'integrated development environment'
print(diccionario)


#recorrer elementos de un diccionario (solo la llave)
for termino in diccionario:
    print(termino)

#recorrer elementos de un diccionario (valor y llave)
for termino,valor in diccionario.items():
    print(termino, ':' ,valor)


#recorrer elementos de un diccionario solo los valores (values)
for valor in diccionario.values():
    print(valor)

#recorrer elementos de un diccionario solo las llaves (keys)
for termino in diccionario.keys():
    print(termino)

#comprobar existencia de algun elemento

print('IDE' in diccionario)

#agregar elemento/ no se pueden agg llaves duplicadas porque se sobreescribe y queda la ultima agregada

diccionario['PK']= 'Primary Key'
print(diccionario)

#remover diccionario

diccionario.pop('DBMS')
print(diccionario)

#limpiar diccionario
diccionario.clear()
print(diccionario)

#eliminar diccionario

del diccionario