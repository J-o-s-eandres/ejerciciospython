casos_favorables=int(input("Ingrese la cantidad de casos que serian favorables en el juego para ganar: "))
casos_posibles=int(input("Ingrese la cantidad de casos posibles que se pueden dar en el juego: "))

probabilidad = (casos_favorables/casos_posibles) *100

print(probabilidad,'%')



