

n = 5
# ________________________________________
for i in range(0,n):
    sumatoria = n * (n + 1) / 2

print sumatoria

# print 5 % 2  , 5 / 2

# ________________________________________

suma = 0
if n % 2 == 0 :

    # si es spar
    for i in range(0, n / 2):
        suma += (n + 1)

elif n % 2 != 0 :
    # si es impar

    for i in range(0, (n-1) / 2):
        suma += (n + 1)

    suma = suma + (round(n / 2) + 1 )

print suma

# ___________________________________________



# referencias

# https://www.cplusplus.com/forum/articles/3638/
#
# http://www.clivemaxfield.com/diycalculator/sp-round.shtml
#
# https://en.wikipedia.org/wiki/Rounding
#
# http://www.allmathwords.org/es/m/median_statistics.html
