#solicitar al usuario un numero n y calcular n+ nn + nnn
#n = 3 => 3 + 33 + 333 = 369

n =int(input('escriba el valor de n: '))

nn= int('{}{}'.format(n,n))
nnn=int('{}{}{}'.format(n,n,n))

suma =n + nn +nnn

print(suma)