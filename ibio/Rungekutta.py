import numpy as np
import matplotlib.pyplot as plt

def main(x0, y0, dt):

    x = []
    y = []
    x0=1.0
    y0=0.0
    x.append(x0)
    y.append(y0)
    t = [0.0]

    i=0

    while t[i] < 50:

        t.append(t[i]+dt)
        x.append(func_x(x[i], y[i], dt))
        y.append(func_y(x[i], y[i], dt))

        i = i + 1


    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color='r')
    plt.show()



def func_x(xi, yi, dt):

    dx = yi
    xj = xi+dx*dt
    return xj


def func_y(xi, yi, dt):

    k1 = func_f(xi, yi, dt)
    k2 = func_f(func_x(xi, yi, dt/2), yi+k1/2, dt)
    k3 = func_f(func_x(xi, yi, dt/2), yi+k2/2, dt)
    k4 = func_f(func_x(xi, yi, dt), yi+k3, dt)

    yj = yi + (k1+2*k2+2*k3+k4)/6

    return yj


def func_f(x, y, dt):

    dy =-x + y*(1-pow(x, 2))
    u = dy*dt

    return u

#初期値と刻み幅を入力してmain関数(数値計算を行う関数)に渡す
main(1.0, 0.0, 0.25)
