
a = [1,2,3,4]
b = [1,2,3,4,5]

# print len(b) 4
filas = len(a)
columnas = len(b)



# matrizP = []
# for a in range(len(a)): # num filas
#     matrizP.append([0] * len(b) )  # numero de columnas
# print matrizP
#
# for i in range(filas):
#     for j in range(columnas):
#         # matrizP[i][j] = [a[i] , b[j] ]
#
#         matrizP.append( a[i] , b[j])
#

matrizP = []

# for i in range(filas):
#     matrizP.append([])
#     for j in range(columnas):
#         valor = [a[i] ,b[j] ]
#         matrizP.append( valor )
#
# print matrizP


print "otra forma   "

for i in range(filas):
    matrizP.append([])
    for j in range(columnas):
        valor = [a[i] ,b[j] ]
        matrizP[i].append( valor )

# print matrizP

for i in range(filas):
    for j in range(columnas):
        if i != j :
            print matrizP[i][j]

# str = " "
# for fila in matrizP:
#     print ("[ "  ,  " ")
#
#     for element in fila :
#
#         str.join(element)   #print type(element)
#         print ("{:8.2f}".format( float(element) ) )
#
#     print " ] "

# strMatriz = " "
# strMatriz.join(matrizP)
#
#
# for fila in strMatriz:
#     print ("[ "  ,  " ")
#
#     for element in fila :
#            #print type(element)
#         print ("{:8.2f}".format( float(element) ) )
#
#     print " ] "

# https://www.askpython.com/python/list/list-to-string
# https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
# https://www.youtube.com/watch?v=tq8XsNjkyec  https://www.youtube.com/watch?v=azldFoUKxQA