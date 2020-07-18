




def palindromo1(cadena):
    minuscula = cadena.lower()  # pasar a minuscula
    palabras = minuscula.split()

    listaPlana = []
    for p in palabras:
        q = p.strip(".").strip(",")  # quitar puntos y comas
        listaPlana.append(q)
    print(listaPlana)

    # pasar a cadena
    cadenaPlana = "".join(listaPlana)
    print(cadenaPlana)

    cadenaPlana = cadenaPlana.replace("à", "a").replace("è", "e")  # reemplazar tildes
    print(cadenaPlana)

    # revertir cadena
    elPalindromo = cadenaPlana[::-1]

    if cadenaPlana == elPalindromo:
        print(" Son palindromos ")
    else:
        print(" no son palindromos")

def palindromo2(cadena):
    minuscula = cadena.lower()  # pasar a minuscula
    palabras = minuscula.split()

    listaPlana = []
    for p in palabras:
        q = p.strip(".").strip(",")  # quitar puntos y comas
        listaPlana.append(q)
    print(listaPlana)

    # pasar a cadena
    cadenaPlana = ""

    for letra in minuscula:  # reemplazando el metodo join
        if letra.isalpha():  #si es caracter alfabetico
            cadenaPlana += letra

    cadenaPlana = cadenaPlana.replace("à", "a").replace("è", "e")  # reemplazar tildes
    print(cadenaPlana)

    # revertir cadena
    elPalindromo = cadenaPlana[::-1]

    if cadenaPlana == elPalindromo:
        print(" Son palindromos ")
    else:
        print(" no son palindromos")

cadena = " anità lava. La tina"  #  " anità lava. La tina"
palindromo1(cadena)
palindromo2(cadena)
#_______________________________________________________________________________

def reverseList(list):
    if len(list) == 0:  # si no es 1
        return []

    return [ list[-1]] + reverseList( list[:-1] )

def reverseList1(list):
    rev= []
    # print (len(list) - 1 )  # seria 4

    #for i in range( len(list) - 1 , -1 , -1  ): # range (start stop step) https://www.w3schools.com/python/ref_func_range.asp
         #rev = rev + list(i)
    #return rev
    #return list = [ list[i] for i in xrange(len(list) - 1, -1, -1) ]


milista = [1 , 2 , 3 , 4 , 5]
a = reverseList(milista) ; print(a)
b = reverseList1(milista); print(b)

# https://www.pythond.com/27441/como-puedo-revertir-una-lista-usando-la-recursividad-en-python.html
# https://www.educative.io/edpresso/how-do-you-reverse-a-string-in-python

# _______________________________________________________________________________

def factoresNumero(n):
    for i  in range(1 , n):
        if n % i == 0 : # si son iguales
            print(i)

N = 10
factoresNumero(N)
# _______________________________________________________________________________

def piramideMedia(filas):
    for i in range(0 , filas):
        for j in range(0 , i + 1):
            print ("*", end= "")  # end quita el new line o espaciado
        print("\r")

numeroFilas = 6
piramideMedia(numeroFilas)