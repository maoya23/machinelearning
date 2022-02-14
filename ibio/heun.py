#ホイン法によって微分方程式を解く

import numpy as np
import matplotlib.pyplot as plt

def main(x0, y0, dt):
    x = []
    y = []

    x.append(x0)
    y.append(y0)
    t = [0.0]
    i = 0

    while t[i] < 50:

        t.append(t[i] + dt)
        x.append(func_x(x[i], y[i], dt))
        y.append(func_y(x[i], y[i], dt))
        i = i + 1


    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color='g')
    plt.show()


def func_x(xi, yi, dt):
    dx = yi
    xj = xi + dx * dt
    return xj


def func_y(xi, yi, dt):
    k1 = func_f(xi, yi, dt)
    k2 = func_f(func_x(xi, yi, dt), yi + k1, dt)
    yj = yi + (k1 + k2) / 2
    return yj


def func_f(x, y, dt):
    dy = -x + y * (1 - pow(x, 2))
    u = dy * dt
    return u

main(1.0, 0.0, 0.25)
