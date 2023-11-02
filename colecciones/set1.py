#no mantiene un orden , no permite almacenar elementos duplicados,no se pueden modificar
#los elementos dentro de un set , pero si se pueden agregar mas elementos o eliminarlos
#no hay indice para ordenar , no mantiene un orden (aleatoreamente manda elementos)
planetas = {'Marte', 'Tierra','Venus','Jupiter','Saturno'}

#largo(cantidad de elementos inicia desde 1 normal)
print(planetas) 

#revisar si un elemento esta presente ,devuelve un valor booleano
print('Marte' in planetas)

#agregar elemento

planetas.add('Urano')
planetas.add('Urano')#asi agg otra vez este planeta no se duplica
print(planetas)

#eliminar elemento/ si queremos eliminar un elemento que no existe nos arroja keyError
planetas.remove('urano')
print(planetas)

#eliminar sin errores por inexistencia
planetas.discard('Jupitiando')# esta funcion tambien sirve para eliminar y no da error en dado caso no consiga el elemento
print(planetas)

#limpiar set
planetas.clear()
print(planetas)


#eliminar set / como no existe el set dara error si lo mandas a imprimir
del planetas

