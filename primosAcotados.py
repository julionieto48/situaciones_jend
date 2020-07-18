
n = 30; numeros = [0] * (n)
for i in range(n):
    numeros[i] = i + 1
#print(numeros)

primos = [0] * n
noprimos = [0] * n
for j in range(2,n):
    noprimos[j] = j + j

print(noprimos)