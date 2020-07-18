# intercambio
# a = 1 ; b = 5 ; aux = 0
# aux = a ; print ("aux :") ; print (aux)
# a = b   ; print ("a :")   ; print (a)
# b = aux ; print ("b :")   ; print (b)


audio_input = [1,2,3,4,5,6,7,8] ; # print(audio_input)

# crear copia
copia = [0] * len(audio_input) #llenar de ceros la copia

for i in range(len(audio_input)): # range arranca desde 0 = len(arreglo) - 1
    copia[i] = audio_input[i]
#print(copia)

# crear linea de delay de la copia
firstDelayLine = [0] * (len(copia) + 1)
for i in range(len(copia)): # range arranca desde 0 = len(arreglo) - 1
    firstDelayLine[i + 1] = copia[i]
#print(firstDelayLine)

secondDelayLine = [0] * (len(copia) + 2)
for i in range(len(copia)): # range arranca desde 0 = len(arreglo) - 1
    secondDelayLine[i + 2] = copia[i]
#print(secondDelayLine)

thirdDelayLine = [0] * (len(copia) + 3)
for i in range(len(copia)): # range hace que arranque desde 0 = len(arreglo) - 1
    thirdDelayLine[i + 3] = copia[i]
#print(thirdDelayLine)


#_________________________________________________________________________

# objetivo : hacer linea de  delay n

input = [1,2,3,4]
nCopia = [0] * len(input)
# se copia la senal original como si fuese el circular buffer
for i in range(len(input)):
    nCopia[i] = input[i]
print(nCopia)

n = 2  # cantidad de retrazos

# nDelayLine = [0] * (len(nCopia) + n)
# for i in range(len(nCopia)):
#     nDelayLine[i + n] = nCopia[i] *0
# print(nDelayLine)


nDelayLine = []
# volver delay line una matriz
for i in range( (len(nCopia) + n) ):
    nDelayLine.append( [0] * (len(nCopia) + n ) )

print(nDelayLine)

for i in range( (len(nCopia) + n)):
    for j in range((len(nCopia) + n)):
        nDelayLine[i][j] = nCopia[i]

print(nDelayLine)





# https://www.youtube.com/watch?v=S18iVRd7Wf4
# https://www.youtube.com/watch?v=XKDSwibZfYA
# https://www.youtube.com/watch?v=yVL1gViXq6w&t=413s
