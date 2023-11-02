#crear una funcion para evaluar un numero y realizar una operacion 

'''def diferencia(n):
    if n <=15:
       return 15 -n
    else:
        return(15-n)*2

print(diferencia(8))
print(diferencia(20))'''


#crear funcion para determinar si un numero es cercano a 1000 o a 2000

def cercania(n):
    return (abs(1000 -n)<100) or (abs(2000 -n)<100)

print(cercania(1990))
print(cercania(990))