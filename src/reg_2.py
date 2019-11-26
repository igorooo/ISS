import numpy as np
import matplotlib.pyplot as plt

T = 10
h = 0.001
a = 0.5
hist = 5
x0 = 40
X = 20 #treshold


steps = (int)(T / h)

x = np.zeros((steps))
v = np.zeros((steps))
t = np.zeros((steps))
x[0] = x0
v[0] = 0
t[0] = 0



for i in range(1, steps):
    x[i] = x[i-1] - h*(a*x[i-1] - v[i-1])




    """
    if x[i] > X + hist and v[i-1] != 0:
        v[i] = 0
        print(x[i], end='1st if ->')
        print(i)

    if x[i] < X - hist and v[i-1] == 0:
        v[i] = x0*2#x0*h
        print(x[i],end=' 2nd if ->')
        print(i, end=' v[i]')
        print(v[i-1])
        print(v[i])
        """

    t[i] = t[i-1] + h


# print(t)
# print(v)

plt.plot(t, x, label='x label')
#plt.plot(t, v, label='v label')
plt.legend()
plt.show()
