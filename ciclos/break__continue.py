#Break
cadena= "Patriarca"

for letra in cadena:
    if letra =='a':
        print(f'letra: {letra}')
        break # una vez encuentra la primera "A"se acaba (rompe) el ciclo(una vez conseguimos lo que queremos podemos romper el ciclo)

else:
    print("Fin del ciclo")



'''for i in range(20):
    if i %2 ==0:
        print(f'Valor: {i}')'''

#Continue

'''for i in range(6):
    if i %2 !=0:
        continue
    print(f'Valor: {i}')'''