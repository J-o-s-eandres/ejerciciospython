import mysql.connector

conexion1= mysql.connector.connect(host="localhost",
                                         user="root",
                                        passwd="",
                                        database="herramientas")
cursor1=conexion1.cursor()

bus=int(input("Ingrese el DNI que desea consultar: "))

cursor1.execute("select *from productos where codigo_product={0}".format(bus)) 


for fila in cursor1:
    print(fila)

conexion1.close()