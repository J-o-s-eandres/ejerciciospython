import mysql.connector
conexion1=mysql.connector.connect(host="localhost",user="root",passwd="",database="colegio")
cursor1=conexion1.cursor()

bus=int(input("Ingrese el DNI que desee buscar: "))

cursor1.execute("select *from alumnos where dni={0}".format(bus))

for fila in cursor1:
    print(fila)

nombre=str(input("Escriba el nuevo nombre: "))
apellido=str(input("Escriba el nuevo apellido: "))
edad =int(input("Escriba la nueva edad: "))
telefono=int(input("Escriba el nuevo numero de telefono: "))

sql="UPDATE alumnos SET NOMBRE='{0}',apellido='{1}',edad='{2}', telefono='{3}' WHERE dni='{4}'".format(nombre,apellido,edad,telefono,bus)
cursor1.execute(sql)
conexion1.commit()
conexion1.close()