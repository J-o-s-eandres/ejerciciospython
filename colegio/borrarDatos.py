import mysql.connector


conexion1=mysql.connector.connect(host="localhost",user="root",passwd="",database="colegio")
cursor1=conexion1.cursor()

bus=int(input("Ingrese el DNI que desee buscar: "))

cursor1.execute("select *from alumnos where dni={0}".format(bus))

for fila in cursor1:
    print(fila)

sql = "DELETE FROM alumnos where dni={0}".format(bus)
cursor1.execute(sql)
conexion1.commit()
print("elemento borrado............")
conexion1.close()