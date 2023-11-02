def calcularImc(peso,altura):
    altura = altura /100
    imc = peso /(altura*altura)
    return imc
    if imc <=20:
        print("Estas Delgado")

    elif imc >= 20 and imc <25 :
     print('peso normal')

    elif imc >= 26 and imc <30 :
        print('tienes sobrepeso')

    elif imc >=30:
        print('obesidad')

calcularImc(150,185)