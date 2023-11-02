#archivo= open('texto.txt','a')#//creamos y abrimos el archivo

#archivo.write("texto de prueba en el archivo")#editamos el archivo

#archivo.close()#cerramos el archivo




archivo = open("texto.txt",'r')#archivo de lectura
print(archivo.read())#imprimir contenido del archivo