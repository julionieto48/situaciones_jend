

def mcd(a , b ):

    if a == b :
        return a   # eleccion entre a o b

    elif a > b :   # si el primer temrino es mayor a%b
        return  mcd(a-b , b)   #  x - y es positivo
    else:
        return  mcd(a , b - a)

def mcm(a,b):
    return (a * b) / mcd(a,b)


#a , b = input("ingresar 2 numeros: ")
a , b = 2322 , 654
a = int(a)
b = int(b)

print "Maximo comun divisor es: " + str ( mcd(a , b))
print "Maximo comun divisor es: " , mcd(a,b)
print "minimo comun multiplo es : " + str ( mcm(a , b)  )

#_________________________
# def swapMinor(a, b):
#     # pq voy a hacer a % b
#     if b > a :
#         a , b = b , a  # como en c++   a
#         return a , b


def mcd1(a , b):

    if b > a :
        # a , b = swapMinor( a , b )
        a = a + b ; b = a - b ; a = a - b
        #print a , b

    if a > b :
        if a % b == 0:
            return b
        else:
            c = a % b
            b = a, c = b
            return  


print "Maximo comun divisor es: " + str ( mcd1(a , b))



