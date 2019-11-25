import numpy as np
import matplotlib.pyplot as plt

h = 1
T = 20
steps = (int)(T/h)
x = []
y = []
t = []

a0 = 0
a1 = 1
x0 = 1
y0 = 0

x.append(x0)
y.append(y0)

print(x)
print("\n")
print(y)

for i in range(steps):

    x.append(x[i] + h*(y[i]))
    y.append(y[i] + h*(-a0 * x[i] - a1 * y[i]))

    print(x[i], end='\n')
    print(y[i], end='\n\n')
