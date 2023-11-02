import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="colegio") 
cursor1=conexion1.cursor()
cursor1.execute("select * from alumnos") 
print("lista")
for fila in cursor1: 
    print(fila) 
conexion1.close()


