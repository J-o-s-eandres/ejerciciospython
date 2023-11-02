historial= [
    [23.3, 55.3, "2022/12/02 01:55:10"],
    [23.5, 55.6, "2022/12/02 01:55:25"],
    [23.1, 56.2, "2022/12/02 01:55:35"],
    [23.7, 56.9, "2022/12/02 01:55:41"],
    [25.2, 57.5, "2022/12/02 01:55:52"],
    [26.1, 58.4, "2022/12/02 01:56:03"],
    [27.3, 59.1, "2022/12/02 01:56:15"]
]

longitud = 0
latitud = 1
fecha= 2

for coordenada in historial :
    print(coordenada)#recorre todo
    print(coordenada[longitud])#recorre solo longitud
    print(coordenada[latitud])#recorre solo latitud
    print(coordenada[fecha])#recorre solo fecha
#print(historial[1][fecha])