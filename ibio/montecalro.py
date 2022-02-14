import random
import numpy as np
import matplotlib.pyplot as plt

point=0
N=100000

for i in range(N):
    x=np.random.random()
    y=np.random.random()

    if x*x+y*y<1.0:
        point+=1
        plt.plot(x,y,'ro')
    else:
        plt.plot(x,y,'bo')
    
    pi=point*4.0/N

print(pi)

plt.gca ().set_aspect('equal',adjustable='box')

plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

