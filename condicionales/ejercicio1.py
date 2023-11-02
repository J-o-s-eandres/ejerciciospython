#concatenar cadenas
'''cantante = "Canserbero" 
cantante2 ="Lil Supa"
print("Mi cantante favorito es " + cantante + " y " + cantante2)
print("mi cantante favovorito es :", cantante,"y",cantante2)'''
#---------------------------------------------------------------------------------------------------------
'''
Booleanos 
a = 4 < 10
print(a)

if a:
    print("El Resultado  fue verdadero")
else:
    print("El Resultado fue falso")'''

#----------------------------------------------------------------------------------------------------------
'''num1 = int(input("Escribe el primer numero: " ))
num2 = int(input("Escribe el segundo numero: "))

resultado = num1 + num2
print("La suma de" ,num1, "+",num2,"es =",resultado)'''

#--------------------------------------------------------------------
#EJERCICIO : PREGUNTALE AL USUARIO COMO ESTUVO SU DIA
 
EstadoDia= int(input("Califica tu dia (del 1 al 10): "))

if EstadoDia == 10 or EstadoDia ==9:
    print(f"Tu dia a estado genial : {EstadoDia}/10")

elif EstadoDia  == 8 or EstadoDia ==7 or EstadoDia==6:
    print(f"tu dia estuvo bastante bien : {EstadoDia}/10")

elif EstadoDia ==  5 or EstadoDia ==4 :
    print(f"Hay Dias  buenos y Dias malos : {EstadoDia}/10")

elif EstadoDia  == 3 or EstadoDia==2 or EstadoDia==1:
    print(f"Mañana sera otro dia : {EstadoDia}/10")

else:
    print("valor fuera de rango. solo  valores del ( 1 al 10)")







   