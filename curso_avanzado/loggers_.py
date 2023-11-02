# Logs , bítacoras
# Python provee una biblioteca que nos permite trabajar con logs basicos
# Los logs son utiles cuando los programas se vuelven mas completjos
# Nos sirven para conocer problemas, ayudarnso en el debug y problemas de desempeño

# Exiten diferentes niveles de logging dependidnedo de la importancia
# NOTSET=0, DEBUG=10, INFO=20, WARN=30, ERROR=40 Y CRITICAL=50

# El formateador del log le coloca al mensaje del log informacion que da contexto(archivo, línea, método, hilo y proceso)

# El handler es el componente que muestra o escribe el log
# Puede hacerlo en un archivo FileHandler, en la consola StreamHandler ó por email SMTPHandler, son los mas comunes 
# El handler tiene dos campos : el formateador y el nivel
# El nivel filtra a los logs inferiores y el formateador es el que le coloca el mensaje 

# Para crear un logger tenemos que obtenerlos de getLogger()
# El logger tiene tres campos
# Propagación -> decide si el log se debe propagar al padre del logger
# Nivel -> Se usa para filtrar logs menos importantes
# Handlers -> La lista de handlers a los que sera enviado el log
# esto permite tener un archivo para los DEBUG y un email para los CRITICAL

# El logger se identifica por el nombre y cada vez que lo usabmos tenemos el mismo objeto
 
# Los loggers trabajan en un sistema jerarquico , teniendo hasta arriba al root logeer Logging.rppt

# Su nivel es WARN y loggers mas bajo son ognorados

# Por default cuando un logger es creado se coloca como hijo del root

# El  nivel efectivo es el mismo que el nivel si el nivel no es NOTSET
# El nivel efectivo es el mismo que el antepadado mas cercano si el nivel es NOTSET y el antepasado no es NOTSET


#Importamos la biblioteca
import logging

#creamos el logger 
miLogger= logging.getLogger("miLogger")

#Por defecto titne el nivel NOTSET
# lo verificamos
assert miLogger.level== logging.NOTSET

#Entonces su nivel efectivo debe de ser el del antepasado mas cercano
# En este caso root, y root tiebe nivel WARN, lo verificamnos
assert miLogger.getEffectiveLevel()==logging.WARN


#Creamos un StreamHandler para usarlo en la consola
# El log se despliega en la consola
handlerConsola = logging.StreamHandler()

# lo adicionamos al handler
miLogger.addHandler(handlerConsola)


# Este mensaje si se muestra en el log pues es del nivel 
miLogger.warning('mensaje desde el warn')

# este mensaje no se muestra en el log pues es de mas bajo nivel
miLogger.debug('mensaje desde el nivel debug')


# Cambiamos el nivel a DEBUG 
# para tener nivel WARN de nuevo, hay que colocarlo manualmente o resetear el kernel 
# el nivel del logger no se resetea al volver a ejecutar el programa 
miLogger.setLevel(logging.DEBUG)

#ahora si se muestra este mensaje en el log
miLogger.debug("Segundo mensaje desde el nivel debug")