# JSON -> JavaScript Object Notation
# Es un formato para guardar y transferir datos
# Es muy utilizado en la web y python provee mecanísmos para poder trabajar con el.


# Python           ->      JSON 
# dict             ->     object
# list , tuple     ->     array
# str              ->     string 
# int, log , float ->     number 
# True, False      ->     true , false 
# None             ->     null

# importamos la biblioteca 
import json

# Leemos un archivo json 
with open('fruta.json','r') as archivo:
    manzana=json.load(archivo)

print(manzana)
print(type(manzana))


##########Convertimos un diccionario en un objeto JSON 


naranja ={'id': 'ft02',
            'nombre':'Naranja', 
            'color': ['naranja', 'amarilla'],
            'costo':8.9,
            'children': 'false'
}


#para convertir usamos dump
naranjaJson= json.dumps(naranja)

# vemos el resultado
print(naranjaJson)


print('-----------------------------------------------')


#Otra forma
naranjaJson2 = json.dumps(naranja, indent=4, separators=(';' , '= '),sort_keys=True)
print(naranjaJson2)


#ahora vemos como salvar a disco
with open('naranja.json', 'w') as archivo:
    json.dump(naranja,archivo)