from cProfile import run


def run():
    my_list = [1, "Holis", True, 4.5]
    my_dict = {"Firstname": "Joseandres", "lastname":"Montesino"}

#Lista de diccionarios
    super_list = [
        {"Firstname": "Joseandres", "lastname":"Montesino"},
        {"Firstname": "Jose", "lastname":"Montesino"},
        {"Firstname": "Josh", "lastname":"Montesino"},
        {"Firstname": "Juan", "lastname":"Montesino"},
        {"Firstname": "seynet", "lastname":"Montesino"},
        {"Firstname": "Barbara", "lastname":"Montesino"},
        {"Firstname": "Esbelia", "lastname":"Montesino"},
        {"Firstname": "Adriana", "lastname":"Hernandez"}
    ]
#diccionario de lista
    super_dict={
        "natural_nums" : [1,2,3,4,5,6,7,8,9],
        "integer_nums" :[-1,-2,0,1,2],
        "floating_nums": [1.1,2.2,4.4]
    }


    for key , value in super_dict.items():
        print(key, "-" , value)


    for dict in super_list[0]():
        print(dict)  
if __name__ == '__main__':
    run()