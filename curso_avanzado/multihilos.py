#importamos las bibliotecas

from threading import Thread
import os
import winsound
import time

#esta es la funcion que se ejecutara en cada proceso
def funcion(numero):
    for n in range(10):
        valor = n*n+n
        print(valor , '----->',numero)
        winsound.Beep(2500,100)

#Para observar la ejecucion debemos de ejecutar en una consola y colocamos el main para facilitar todo

if __name__== '__main__':
    #en esta lista guardamos los hilos
    hilos =[]

    #obtenemos la cantidad de cores que tenemos

    cores = os.cpu_count()
    print('Tienes : ', cores, 'cores')


    print('------ Instanciar')

    #Aqui creamos los hilos

    for n in range(cores):
        #creamos la instancia del proceso
        #asiganmosla funcion a ejecutar y cualquier parametro necesario
        #args se pasa como una tupla
        hilo = Thread(target=funcion, args=(n,))
        #lo adicionamos a la lista de procesos
        hilos.append(hilo)

    print('---------- Ejecutar')
    #Ahora que ya estan instanciado vamos a iniciar su ejecución

    for hilo in hilos:
        hilo.start()

    print('--------- Espera')
    for hilo in hilos:
        hilo.join()

    print('------------ Regresamos a la ejecucion inicial')

    time.sleep(10)