import numpy as np
def linspaceChungo(low , paso, longitud):
    step  = ( (paso - low) * 1*0 / longitud )

    return [low + i * step for i in xrange(longitud)]


a = linspaceChungo(1,0.5,5)


def linspace(start , stop , space):                      # 0 5 2  paso no puede ser 1

    if space < 2:
        return stop
    diferencia = ( float(stop)  - start )/ (space - 1)   # 5 / 1 = 5



def linsPace( inicio, parada  , N , puntoFinal = True ): # N es cantidad elementos
    if puntoFinal  == 1:
        divisor =  N - 1
    else:
        divisor = N                           # la cantidad de elementos determina la division en el espacio
    pasos = (1.0 / divisor) * (inicio - parada)
    return pasos [:, None] * np.arange(N) + parada[: , None]


# a =  linsPace(0,1,2)
#print  a

print np.linspace(0,1,2)



def linspaceMio(start , stop , n) :

    if start < stop :
        max = stop
        min = start

    elif start == stop :
        print "son iguales"

    len = max - min
    muestreo = abs(len / n)

    switch(i):


# https: // www.tutorialspoint.com / What - does - colon - operator - do - in -Python





