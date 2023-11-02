import sys
import time

#Crear 4 Funciones para determinar la secuencia Fibonacci hasta un limite de numero n proporsionado por el usuario
#Crear 1 menu con las 4 opciones para que el usuario pueda elegir a voluntad
#Determinar cual funcion es la mas rapida en tiempo de ejecucion (medir segundos) 

def fibo_aux(n):
    a=0
    b=1
    aux=None

    for i in range(n):
        print(a)
        aux= a #0
        a = b #1 
        b= aux + a  # 0 + 1


def fibo_form(n):
    fibo= [0,1]


    for i in range(2,n):
        fibo.append(fibo[i - 2] + fibo[i-1])

    print(fibo)   


def fibo_r(n):#recursividad: es una funcion que se llama a si misma una cantidad  especifica de veces
    if n==0 or n ==1: #2 primeros valores de la serie fibonacci
        return n
    
    return fibo_r(n-1) + fibo_r(n-2)

def fibo_d(n, memo = {}):
    result = 0

    if n == 0 or n == 1:
        return n

    try:
        result = memo[n]

    except KeyError:
        result = fibo_d(n - 1, memo) + fibo_d(n - 2, memo)
        memo[n]= result 

    return result    


def banner():
    print('''
    *********************************
    *          Fibonacci            *
    *********************************
    1 - Aux
    2 - Formula
    3 - Recursion
    4 - Dynamic Recursion
    ''')
    return int(input('Option: '))

def main():
  option = banner()

  limite =int(input('Ingrese el numero limite: '))

  tiempo_inicial= time.time()  

  if option == 1:
      fibo_aux(limite)
  elif option == 2:
    fibo_form(limite)
  elif option == 3:
    print(fibo_r(limite))
  elif option == 4:
    print(fibo_d(limite))


  tiempo_final= time.time()

  print(f"\n\nTime:{tiempo_final - tiempo_inicial}")

if __name__ == "__main__":
    sys.setrecursionlimit(10010)
    main()   