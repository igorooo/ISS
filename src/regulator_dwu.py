import numpy as np
import matplotlib.pyplot as plt

T = 10
h = 0.01
a = -0.5
hist = 5
x0 = 100
# treshold
X = 20
# POWER
U = 30
# HIST <-H ; H>
H = 2

steps = (int)(T / h)

# function
x = np.zeros((steps))
# controll signal
u = np.zeros((steps))
# time
t = np.zeros((steps))
# error
e = np.zeros((steps))

hUp = np.ones((steps)) * H
hDown = np.ones((steps)) * (-H)

x[0] = x0
u[0] = 1
t[0] = 0
e[0] = X - x0
power = False


for i in range(1, steps):
    x[i] = x[i-1] + h*(a*x[i-1] + u[i-1])
    t[i] = t[i-1] + h
    e[i] = X - x[i]

    if not (e[i] < H and e[i] > -H):
        if e[i] > 0:
            power = U
        else:
            power = 0

    u[i] += power


plt.plot(t, x, label='function')
plt.plot(t, u, label='control signal')
plt.plot(t, e, label='error')
plt.plot(t, hUp, label='H upper')
plt.plot(t, hDown, label='H lower')
plt.legend()
plt.show()
