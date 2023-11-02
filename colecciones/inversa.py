#obtener la representacion inversa de una cadena de caracteres

cadena = input('Ingrese una cadena de texto: ')

for i in range(len(cadena) -1 ,-1, -1):
    print(cadena[i], end='')


print()
#notacion de slaicin

print(cadena[::-1])