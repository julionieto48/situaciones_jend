def primosCriba(n):

    a = [False] * 2 + [True] * (n-1)    # lista booleana de a pares

    for (i,primo) in enumerate(a):     # enumarate como una forma alternativa de iteracion aun elemento itrable en este caso a
        if primo:
            for x in range(i * i, n, i):
                a[x] = False
    return [j for (j, k) in enumerate(a) if k == True]

a = primosCriba(30) ; print a
#_______________________________//___________________________________

def primosCribaVone(n):

    numeros = [False] * 2 + [True] * (n-1)    # lista booleana de a pares en este caso de forma aleatoria esta desicion
    ultimoPrimo = 2                     # es el valor del salto que se realiza
    i = ultimoPrimo                     # como el valor del salto esta detemrinado por el primo en el qu enos encontramos
    j = ultimoPrimo

    while ultimoPrimo ** 2 <= n :        # ultimo primo * ultimo primo el proceso de seleccion finaliza cuando el cuadrado del ultimo numero primo obtenido (last_prime_number) es mayor que el argumento.
        i += ultimoPrimo                 # aumento iteracion

        while i <= n :
            numeros[i] = False           # se tacha o asigna valor falso a elementos que coinciden con el ultimo primo encontrado
            i += ultimoPrimo


        # obtener el numero siguiente al numero tachado como falso, numero primo obtenido (last_prime_number) que no este tachado.
        j += ultimoPrimo + 1
        while j < n :
            if numeros[j]:
                ultimoPrimo = j
                break
            j += 1
        i = ultimoPrimo

    return [i + 2 for i, not_crossed in enumerate(numeros[2:]) if not_crossed]

a = primosCribaVone(30) ; print a











# https://www.geeksforgeeks.org/enumerate-in-python/
# https://es.wikipedia.org/wiki/Criba_de_Erat%C3%B3stenes
# https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
# https://www.geeksforgeeks.org/sieve-of-eratosthenes/
# https://recursospython.com/guias-y-manuales/obtener-lista-numeros-primos/
# https://www.python-course.eu/python3_for_loop.php
# https://stackoverflow.com/questions/2582732/time-complexity-of-sieve-of-eratosthenes-algorithm/