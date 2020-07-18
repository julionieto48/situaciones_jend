import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

arreglo = [1,1, 2, 2, 2, 3, 5 ]

# _______________________________________________________________
# busqueda lineal del elemento
def contadorOcurrencia(array, n, x):
   out = 0

   for i in range(0, len(arreglo)):

       if x == array[i]:
           out += 1 # operador de asignacion
   return out


contado = contadorOcurrencia(arreglo,0,2) ; print(contado)
# _______________________________________________________________
num_bins = 5
n, bins, patches = plt.hist(arreglo , num_bins, facecolor = 'blue', alpha = 0.5)
plt.show()
# _______________________________________________________________
def contadorElementos(array):  # se ingresa secuencia y retorna un diccionario def contadorElementos(array) -> dict:
    hist = {}                          # diciconario vacio

    for i in array:
        hist[i] = hist.get(i , 0) + 1 # si el valor corresponde lo coloca d elo contrario es un cero
    return  hist

contados = contadorElementos(arreglo) ; print(contados)

# https://www.geeksforgeeks.org/program-make-histogram-array/
# https://www.youtube.com/watch?v=OpTwGLVCtHQ
# https://www.tutorialspoint.com/python/dictionary_get.htm
# https://stackoverflow.com/questions/4515874/searching-for-a-fast-efficient-histogram-algorithm-with-pre-specified-bins#4516105