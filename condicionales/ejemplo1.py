#calculadora de IMC

#IMC=peso/(Altura x Altura)


#<19:delgado, entre 20-25:normal,entre 26-30:sobrepeso,> 30:obeso


peso= int(input('Ingrese su peso en Kg: '))
altura = int(input('ingrese su altura en cm: '))
alturaMetros =altura/100
imc=peso / (alturaMetros * alturaMetros)


if imc <=20:
    print("Estas Delgado")

elif imc >= 20 and imc <25 :
    print('peso normal')

elif imc >= 26 and imc <30 :
    print('tienes sobrepeso')

elif imc >=30:
    print('obesidad')