import mysql.connector

class Conector:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="colegio")
        return conexion
        
    def agregar_alumno(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into alumnos(dni) values (%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre from alumnos where dni=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()
