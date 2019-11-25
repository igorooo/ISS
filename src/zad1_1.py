import numpy as np
import matplotlib.pyplot as plt

T = 10
h = 0.5
x_pocz = 0.01
iter = (int)(T / h)

t = []
x = []
t.append(h)
x.append(x_pocz)

prog = 1

a = np.random.normal(loc=0,scale=1.0)
a = np.random.uniform()

for i in range(iter-1):
    x.append(x[i] + h * (-a * x[i] ))
    t.append(t[i]+h)
    #if x[i+1] < prog:
    #    x[i+1] = x_pocz

plt.plot(t[:],x[:],'o')
plt.show()
