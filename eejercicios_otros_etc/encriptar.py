def encriptar(texto):
    #print('El texto a encriptar es: ' + texto)
    textofinal= ''
    for letra in texto:
        ascii=ord(letra)
        ascii += 1
        textofinal += chr(ascii)
    return textofinal

def desencriptar(texto):
    #print('El texto a desencriptar es: '+ texto)       
    textofinal= ''
    for letra in texto:
        ascii=ord(letra)
        ascii -= 1
        textofinal += chr(ascii)
    return textofinal

#encriptar("prueba")
#desencriptar('Pxrxuxexbxax')



def encriptarArchivo(ruta):
    archivo = open(ruta,'r')
    texto= archivo.read()
    archivo.close()
    textoEncriptado=encriptar(texto)

    archivo= open(ruta,"w")
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo se encripto correctamente")


def desencriptarArchivo(ruta):
    archivo = open(ruta,'r')
    texto= archivo.read()
    archivo.close()
    textoDesencriptado=desencriptar(texto)

    archivo= open(ruta,"w")
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo se desencripto correctamente")

#encriptarArchivo()
#desencriptarArchivo()

respuesta= input("Presione 'E' para encriptar ,o 'D' para desencriptrar sus archivos: ")
ruta=input("Ingrese la ruta del archivo a encriptrar o desencriptar: ")


if respuesta == "E":
    encriptarArchivo(ruta)

elif respuesta == "D":
      
    desencriptarArchivo(ruta)

else: 
    print("PARAMETRO INVALIDO")