import  numpy as np


for i in range(1, 20):
    print( ( (2 * i + 6 )/ 2 ) - i  )

print(" ____//___________________//______ ")

for i in range(0, -10, -2):
    print(((2 * i + 6) / 2) - i)

print(" ____//___________________//______ ")

def frange(start, stop, step):
   i = start
   while i < stop:
       yield i
       i += step

for i in frange(0.5, 1.0, 0.1):
    print(((2 * i + 6) / 2) - i)

print(" ____//___________________//______ ")

x = np.array([2,3,1,0])

np.arange(10)

# https://docs.scipy.org/doc/numpy-1.13.0/user/basics.creation.html