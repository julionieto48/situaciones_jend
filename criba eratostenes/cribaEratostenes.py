import math


def primos(N):

    lista = [i for i in range(2, N + 1)]    # lista de enteros desde 2 a 50

    for candidato in range(2 , int( math.sqrt(N)) + 1):
        # print  " raiz de n es:" , int( math.sqrt(N) + 1 ) 8
        # print  candidato      2 3 4 5 6 7 none

        if candidato in lista:
            prueba = candidato ** 2
            print "prueba es:" , prueba

            while prueba <= N :       # este proceso me ayudar a aescoger el siguiente primo candidato y ademas cuando la potencia  # sea mayor se habrna encontrado los primos hasta N
                if prueba in lista :
                    lista.remove(prueba)   # se itera el remove puede que en un futuro coincidan numeros por remover

                prueba += candidato   # se actualiza al siguiente primo de acuerdo a los multiplos que quedan
    return lista



print  primos(5)


# forma tradicional de los primos

def primosDos(N):


    if N > 0:
        for x in range(2, N + 1):  # print range(2, N + 1)  = [2, 3, 4, 5]
            primitosMomochos = []


            aument = 2
            isPrime = True

            while isPrime and aument < x:
                if x % aument == 0:  # si la division es exacta  ejemplo 10/2 =   no es primo ya qu elos primos no pueden tneer ms divisiones exactas
                    isPrime = False
                else:
                    aument = aument + 1   # aument s eva a incrementar hasta que tenga un valor menor el indice x


            if isPrime :
                print  x
                primitosMomochos.append(x)
    return primitosMomochos



print primosDos(5)