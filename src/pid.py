import numpy as np
import matplotlib.pyplot as plt


class PID :

    def funct(self, step, Tmax, f0, ex, fx, Kp, Ki, Kd):
        iterations = (int)(Tmax / step)
        f = np.zeros((iterations))
        error = np.zeros((iterations))
        control = error = np.zeros((iterations))
        time = np.zeros((iterations))

        I = np.zeros((steps))
        D = np.zeros((steps))
        P = np.zeros((steps))

        f[0] = f0

        for i in range(1, iterations):
            f[i] = f[i - 1] + step * fx(f[i - 1], control[i - 1])
            error[i] = ex(f[i])
            time[i] = time[i - 1] + step
            I[i] = I[i - 1] + error[i]
            D[i] = error[i] - error[i - 1]
            P[i] = error[i]

            control[i] = Kp * P[i] + Ki * I[i] + Kd * D[i]

        return f, error, time, control, P, I, D

    def countFitness(self, error):
        fit = 0
        for i in range(error.size):
            fit += abs(error[i])
        return fit





T = 10
h = 0.01
a = -0.5
hist = 5
x0 = 100
# treshold
X = 20


steps = (int)(T / h)



"""for i in range(1, steps):
    x[i] = x[i-1] + h*(a*x[i-1] + u[i-1])
    t[i] = t[i-1] + h
    e[i] = X - x[i]

    I[i] = I[i-1] + e[i]
    D[i] = e[i] - e[i-1]
    P[i] = e[i]

    u[i] = Kp * P[i] + Ki * I[i] + Kd * D[i]"""

"""error_funct = lambda val : 20 - val
f_funct = lambda val1, val2: (a*val1 + val2)
fitness = lambda err, t : abs(err) / t


pid = PID()

x, e, t, u, P, I, D = pid.funct(0.01, 10, 100, error_funct, f_funct, 1, 0.1, 0.1)
print(pid.countFitness(e))
print(I[steps-1])



plt.plot(t, x, label='function')
plt.plot(t, u, label='control signal')
plt.plot(t, e, label='error/P')
plt.plot(t, I, label='Integral')
plt.plot(t, D, label='Derivative')
plt.legend()
plt.show()"""

pid = PID()

error_funct = lambda val : 20 - val
f_funct = lambda val1, val2: (a*val1 + val2)
fitness = lambda err, t : abs(err) / t



x, e, t, u, P, I, D = pid.funct(0.01, 10, 100, error_funct, f_funct, 1, 0.1, 0.1)
print(pid.countFitness(e))
print(I[steps-1])



plt.plot(t, x, label='function')
plt.plot(t, u, label='control signal')
plt.plot(t, e, label='error/P')
plt.plot(t, I, label='Integral')
plt.plot(t, D, label='Derivative')
plt.legend()
plt.show()
