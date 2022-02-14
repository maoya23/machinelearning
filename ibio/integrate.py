import numpy as np

a=float(input("aの値を代入してください:"))
b=float(input('bの値を代入してください:'))
N=10000
S=0

h=np.abs(a-b)/N

for i in range(0,N):
    xi=a+i*h
    xn=a+(i+1)*h
    S+=h*(np.sin(xi)+np.sin(xn))/2

print(S)

