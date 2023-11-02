import json

"""
json_str = '{"nombre": "Joseandres", "apelldio" : "Montesino", "edad": 22, "pais": "Venezuela"}'

print(json_str)
print(type(json_str))


python_dict = json.loads(json_str)

print(type(python_dict))

print(python_dict['edad'])
print(python_dict['nombre'])

"""

"""
data = {
    "nombre" : "Joseandres",
    "edad"  : 22,
    "pais" :"Venezuela",
    "cursos": ["PHP", "C#", "NodeJS", "C++"]
}

json_data = json.dumps(data)
print(type(json_data))
print(json_data)

"""
"""
data = {
    "nombre" : "Joseandres",
    "edad"  : 22,
    "pais" :"Venezuela",
    "cursos": ["PHP", "C#", "NodeJS", "C++"]
}


# json_data=json.dumps(data, indent=4, separators=(",", ":"))
json_data=json.dumps(data, indent=4, separators=(",", ":"),sort_keys=True)
print(json_data)

"""

"""

json_data= json.JSONEncoder().encode({"Lenguajes":["Python", "JavaScript"]})

print(json_data)
print(type(json_data))


python_dict = json.JSONDecoder().decode(json_data)
print(python_dict)
print(type(python_dict))
"""


#convertir la instancia de una clase personalizada aun objeto json
class Curso():

    def __init__(self,codigo,nombre,creditos) :
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos


curso_1 = Curso("90034", "Lenguaje", 4)
print(curso_1)

json_object_data = json.dumps(curso_1.__dict__)
print(json_object_data)
print(type(json_object_data))


python_dict= json.loads(json_object_data)
print(python_dict)
print(type(python_dict))

"""
Equivalencia entre tipo de datos en Python y en JSON (JavaScript)

Python --------- JSON
ditc       ==>  Object
list       ==>  Array
tuple      ==>  Array
str        ==>  String
int        ==>  Number
float      ==>  Number
True       ==>  true
False      ==>  false
None       ==>  null
"""
