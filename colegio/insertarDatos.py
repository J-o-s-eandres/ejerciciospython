import mysql.connector
#conectando a la BD 
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="colegio")

cursor1=conexion1.cursor()

#creando las variables que se van a insertar a los campos de la tabla alumno
Dni=int(input("Ingrese su DNI: "))
nombre=str(input("Ingrese su nombre: "))
apellido=str(input("Ingrese su apellido: "))
edad=int(input("Ingrese su edad: "))
telefono=int(input("Ingrese su numero de telefono: "))
sql="insert alumnos (Dni,nombre,apellido,edad,telefono)\
    values ('{0}','{1}','{2}','{3}','{4}')".format(Dni,nombre,apellido,edad,telefono)

cursor1.execute(sql)

cursor1.execute("select * from alumnos")

print("\t   lista de alumnos\n\t------------------------------")

for fila in cursor1:
    print(fila)

conexion1.commit()
conexion1.close()