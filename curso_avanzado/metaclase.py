#En python a diferencia de otros lenguajes de programacion las clases son objetpd


# una clase define las caracteristicas que tendra el objeto
#una metaclase define las caracteristicas que tendra la clase

#definimos la clase
class miClase():
    pass

#creamos la instancia
uno = miClase()

#vemos cual es el tipo de la instacnia
print(type(uno))


#vemos cual es el tipo de la clase
#Con esto reconocemos que la clase tiene un tipo que es usado para definirla
print(type(miClase))

#Ahora definimos otra clase usando type directamente y obtenemos una instancia


#El primer parametro es el nombre de la clase - representacion interna
#El segundo es la base, si es que hay hertencia
#El ultimo son los atributos

miPrueba = type('Prueba', (), {'valor':10})

print(miPrueba)
print(type(miPrueba))
print(miPrueba.valor)

dos = miPrueba()
print(dos.valor)

#Creamos otra clase para adicionarle un metodo

def miMetodo(self):
    print('hola')

miPruebaM= type('PruebaMetodo',(),{'costo':5, 'miMetodo': miMetodo}) 

tres=miPruebaM()
tres.miMetodo()