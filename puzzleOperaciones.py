import random
import numpy as np



puzz = np.zeros( shape=(3,3) )

#valores determinados para resultado
puzz[0][2]= 5
puzz[1][2]= 6
puzz[2][0]= 3
puzz[2][1]= 8


flag = False ; cont = 1
#
# while flag != False :
#
#     puzz.apend(random.randint(0, 5))
#
#puzz[0][0] = random.randint(0, 5)
#print puzz
flagDos,flagUno = False,False

while flag == False :
    puzz[0][0] = random.randint(0, 5)
    puzz[0][1] = random.randint(0, 5)

    if puzz[0][0] + puzz[0][1] == puzz[0][2]:
        print " primera fila lograda"
        flagUno = True

    puzz[1][0] = random.randint(0, 5)
    puzz[1][1] = random.randint(0, 5)

    if puzz[1][0] + puzz[1][1] == puzz[1][2]:
        print " segunda fila lograda"
        flagDos = True

    if flagUno & flagDos == True :

        flag = True




    cont += 1


print puzz







# print range(len(puzz))







# https://stackoverflow.com/questions/568962/how-do-i-create-an-empty-array-matrix-in-numpy