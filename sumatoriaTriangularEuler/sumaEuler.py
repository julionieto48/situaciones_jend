arregloImpar = [1,2,3,4,5] ; arreglopar = [1,2,3,4,5,6]

total = 0

for i in range(len(arregloImpar)):
    suma = arregloImpar[i] + arregloImpar[-1]
    print suma

    arregloImpar.pop(i) ;  arregloImpar.pop(i +len(arregloImpar) - 1)
    total = total + suma
    #print total

    print arregloImpar

# https://stackoverflow.com/questions/930397/getting-the-last-element-of-a-list
# https://thispointer.com/python-numpy-select-an-element-or-sub-array-by-index-from-a-ndarray/
# https://es.stackoverflow.com/questions/108027/encontrar-el-ultimo-elemento-del-array
# https://es.stackoverflow.com/questions/47764/manejo-de-un-elemento-de-una-lista-en-python
