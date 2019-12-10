import numpy as np
import matplotlib.pyplot as plt


T = 10
h = 0.001



steps = (int)(T / h)

# function
x = np.zeros((steps))
y = np.zeros((steps))
# control signal
u = np.zeros((steps))
# time
t = np.zeros((steps))
# error
e = np.zeros((steps))

# error
I = np.zeros((steps))

# error
D = np.zeros((steps))

# error
P = np.zeros((steps))


X = 2

x[0] = 5
u[0] = 0
t[0] = 0
e[0] = X - x[0]

Kp = 0.1
Ki = 0.5
Kd = 0.1

ui = 0.5
wd = 1


for i in range(1, steps):
    y[i] = y[i-1] + h*x[i-1]
    x[i] = x[i-1] + h*(ui*(1-y[i-1]*y[i-1])*x[i-1] - wd*wd *y[i]) + h*u[i-1]
    t[i] = t[i-1] + h
    e[i] = X - x[i]

    I[i] = I[i-1] + e[i]
    D[i] = e[i] - e[i-1]
    P[i] = e[i]

    u[i] = Kp * P[i] + Ki * I[i] + Kd * D[i]



#plt.plot(t, x, label='x function')
plt.plot(y, x, label='y x function')
#plt.plot(t, u, label='control signal')
#plt.plot(t, e, label='error/P')
#plt.plot(t, I, label='Integral')
#plt.plot(t, D, label='Derivative')
plt.legend()
plt.show()

plt.plot(t, x, label='x function')
plt.plot(t, y, label='y function')

plt.legend()
plt.show()

