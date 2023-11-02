'''a = 4
b = 2

resultado = a ==b
resultado1 = a !=b

print(f'Resultado == : {resultado1}')'''

'''
edadAdulto=18
edad = int(input('Ingresa tu edad: '))
nombre = input('Ingrese su nombre: ')

if edad >= edadAdulto:
    print(f'Adelante {nombre} usted tiene {edad} y puede pasar por unas Cervezas')

else:
    print(f'Alto!! {nombre} usted tiene {edad} años y no puede ingresar , vaya a su casa a tomar jugo')'''
    

# operadores logicos  => not(unario) , and (binario), or (binario)
'''
a = True
b = False
resultado = a and b 
#print(resultado)


resultado = a or b
#print(resultado)

resultado = not a
print(resultado)'''

# EJERCICIO CON AND
'''
valor =int(input('Escribe el valor: '))
min = 0
max = 5

dentroRango = (valor >= min) and (valor <= max)

if dentroRango :
    print(f'El valor {valor} esta dentro del rango')

else:
    print(f'El valor {valor} esta fuera de rango')'''


#EJERCICIO CON OR 

'''vacaciones = False
diaLibre = True

if vacaciones or diaLibre:
    print('Puede Asistir al juego')

else:
    print('No puede Asistir al Juego')'''


#Ejercicio NOT

'''vacaciones = False
diaLibre = False

if not (vacaciones or diaLibre):
   
    print('No puede Asistir al Juego')

else:
    
    print('Puede Asistir al juego')'''


# EJERCICIO TIENDA DE LIBROS

'''NameBook= input("what it the name of the book?: ")
idBook= int(input("What it the ID of the book?: "))
delivery = input("shipping is free (yes / no)?: ")


if delivery == 'yes':
    delivery = True
    if delivery == True:
        delivery ="Yes"


elif delivery == 'no':
    delivery = False
    if delivery == False:
        delivery ="No"
else :
   
    delivery =("wrong value.     expected values (yes / no)")
   

print(f'''
'''
    Book information:
    
    Name: {NameBook}
    idBook: {idBook}
    delivery: {delivery}'''
''')'''