import numpy as np
import matplotlib.pyplot as plt


T = 10
h = 0.01



steps = (int)(T / h)

a = -0.2
X = 25
hist = 10

temperature = 100
u = 0
e = X - temperature
time = 0

x_history = []
e_history = []
time_history = []
u_history = []



for i in range(1, steps):

    x_history.append(temperature)
    e_history.append(e)
    time_history.append(time)
    u_history.append(u)

    temperature = temperature + h*(a * temperature + u)
    e = X - temperature
    time += h

    if not((0 + hist) > e > (0 - hist)):
        if e > 0:
            u = 50
        elif e < 0:
            u = -50


plt.plot(time_history, x_history , label='temperature')
plt.plot(time_history, e_history, label='error')
plt.plot(time_history, u_history, label='control')
plt.legend()
plt.show()



