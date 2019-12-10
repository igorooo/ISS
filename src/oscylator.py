import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize



def minimizePID():
    initial = np.array([1,1,1])

    solution = minimize(calcFunction, initial, method='SLSQP')
    print(solution.x)


def calcFunction(PID_P):
    x, y, e, t, u, P, I, D = funct(step=0.001, Tmax=10, x0=5, y0=0, X=2, PID_P=PID_P)
    return countFitness(e)

def funct(step, Tmax, x0, y0, X, PID_P):
    Kp, Ki, Kd = PID_P[0], PID_P[1], PID_P[2]
    iterations = (int)(Tmax / step)
    x = np.zeros((iterations))
    y = np.zeros((iterations))
    error = np.zeros((iterations))
    control = np.zeros((iterations))
    time = np.zeros((iterations))

    I = np.zeros((iterations))
    D = np.zeros((iterations))
    P = np.zeros((iterations))

    x[0] = x0
    y[0] = y0

    error_funct = lambda val: X - val

    # parameters
    WD = 1
    UI = 0.5

    for i in range(1, iterations):
        y[i] = y[i - 1] + step * x[i - 1]
        x[i] = x[i - 1] + step * (UI * (1 - y[i - 1] * y[i - 1]) * x[i - 1] - WD * WD * y[i]) + step * control[i - 1]
        error[i] = error_funct(x[i])

        time[i] = time[i - 1] + step

        I[i] = I[i - 1] + error[i]
        D[i] = error[i] - error[i - 1]
        P[i] = error[i]

        control[i] = Kp * P[i] + Ki * I[i] + Kd * D[i]

    return x, y, error, time, control, P, I, D


def countFitness(error):
    fit = 0
    for i in range(error.size):
        fit += abs(error[i])
    return fit


T = 10
h = 0.01
x0 = 5
# target value
X = 20
steps = (int)(T / h)


#minimizePID()

PID_PARAM = (1221.31737265, 765.06406742, -71.3437605)

#PID_PARAM = (0.1, 0.1, 0.1)

x, y, e, t, u, P, I, D = funct(step=0.001, Tmax=10, x0=5, y0=0, X=2, PID_P = PID_PARAM )
print(countFitness(e))




#plt.plot(t, u, label='control signal')
#plt.plot(t, e, label='error/P')
#plt.plot(t, I, label='Integral')
#plt.plot(t, D, label='Derivative')

plt.plot(y, x, label='x y')
plt.legend()
plt.show()

plt.plot(t, x, label='x function')
plt.plot(t, y, label='y function')

plt.legend()
plt.show()
