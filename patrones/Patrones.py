n = 4

for i in range(n+1):
    print("*" * i)
print(" \n ")

# range start stop step
for i in range(0, n , 1):
    for j in range (0, i + 1, 1):
        print("*" , end = " " )
    print(" ")

print(" \n ")

for i in range(n, 0 , -1):
    for j in range (0, i , 1):
        print("*" , end = " " )
    print(" ")

print(" \n ")

for i in range(n, -1 , -1):
    for j in range ( i ):
        print(" " , end = " " )
    for k in (i,n):
        print("*", end= " ")
    print(" ")

print(" \n ")

for i in range(n - 1, -1 , -1):
    for j in range ( n - i - 1 ):
        print(" " , end = " " )
    for k in (i + 1):
        print("*", end = " ")
    print(" ")

print(" \n ")

# https://www.youtube.com/watch?v=OjQFZwEBsBY
# https://www.youtube.com/watch?v=YhGP6w-XwYQ&t=358s