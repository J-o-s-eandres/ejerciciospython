import inspect
import moduloEjemplo

# Inspect es una clase con metodos que nos va a permitir obtener informacion de otrs clases (no siempre va a poder obtener informacion)

# Inspect es un módulo de Python que se utiliza para examinar el código fuente de un programa. Esto se logra mediante la inspección de los objetos,
#  atributos y contenido de clases. El módulo inspect también le permite a los usuarios recuperar información relevante sobre el código que se está
#  ejecutando, como la ruta al archivo, la línea actual, la clase, los argumentos del método, etc.


print('------- Clases, objetos y funciones de modulo-------\n')
#buscamos las clases, objetos y funciones de modulo

for nombre, datos in inspect.getmembers(moduloEjemplo):
    #no mostramos los que inicien  con __
    if nombre.startswith('__'):
        continue
    print('Nombre: ', nombre, 'datos: ', datos)


print('\n----- Buscamos las clases en el modulo --------\n')

for nombre, datos in inspect.getmembers(moduloEjemplo, inspect.isclass):
    print('Clase: ', nombre, 'datos: ', datos)

print('\n----- Buscamos los  metodos en unaclase  --------\n')

for nombre, datos in inspect.getmembers(moduloEjemplo.claseBase, inspect.isfunction):
    print('Clase: ', nombre, 'datos: ', datos)
print('--------------')

for nombre, datos in inspect.getmembers(moduloEjemplo.claseHija, inspect.isfunction):
    print('Clase: ', nombre, 'Datos: ', datos)

#obtenemos la documentcaion de la clase
print(moduloEjemplo.claseBase.__doc__)

#obtenemos el codigo fuente de un metodo
print(inspect.getsource(moduloEjemplo.claseHija.miMetodo))

#obtenemos la firma de la funcion, nos indica los parametros
print(inspect.signature(moduloEjemplo.miFuncion))