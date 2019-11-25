import numpy as np
import matplotlib.pyplot as plt

T = 10
h = 0.1
x_pocz = -100
iter = (int)(T / h)

t = []
x = []
t.append(h)
x.append(x_pocz)

for i in range(iter-1):
    a = np.random.normal(loc=0,scale=1.0)
    a = np.random.uniform()
    x.append(x[i] + h * (a*x[i]))
    t.append(t[i]+h)

plt.plot(t[:],x[:],'o')
plt.show()
