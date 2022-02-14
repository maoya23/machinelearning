#オイラー法で次の微分方程式を解け
#dx/dt = y
#dy/dt= -x + y(1-pow(x, 2))
#xの初期値は[1.0]
#yの初期値は[0]

import numpy as np
import matplotlib.pyplot as plt
#初期値と刻み幅を引数に数値計算を行う関数を定義
def main(x0, y0, dt):
    #時刻tにおいてx,yの解を格納するリストの作成
    x = []
    y = []

    #初期値をリストに追加
    x.append(x0)
    y.append(y0)
    #t
    t = [0.0]
    #iで計算回数をカウント
    i=0
    #t=50になるまで繰り返す
    while t[i] < 50:
        #tのリストにdt後のtを追加
        t.append(t[i]+dt)
        #xのリストにdt後のxを追加(計算はfunc_xに飛ぶ)
        x.append(func_x(x[i], y[i], dt))
        #yのリストにdt後のyを追加(計算はfunc_yに飛ぶ)
        y.append(func_y(x[i], y[i], dt))
        #iをカウントアップ
        i = i + 1

    # x,yのリストより関数を図示
    plt.xlabel('x')
    plt.ylabel('y')
    figure=plt.plot(x, y, color='b')
    plt.show()


#引数はx_i、y_i、dt、戻り値はx_i+1として、オイラー法によりdt後のxを計算する
def func_x(xi, yi, dt):
    #問題文よりdtの間のxの変化分は
    dx = yi
    #時間tにおけるxの数値計算量は
    xj = xi+dx*dt
    #x_i+1を返す
    return xj

#引数はx_i、y_i、dt、戻り値はy_i+1として、オイラー法によりdt後のyを計算する
def func_y(xi, yi, dt):
    #問題文よりdtの間のyの変化分は
    dy =-xi + yi*(1-pow(xi, 2))
    #時間tにおけるyの数値計算量は
    yj = yi+dy*dt
    #y_i+1を返す
    return yj

#初期値と刻み幅を入力してmain関数(数値計算を行う関数)に渡す
main(1.0, 0.0, 0.25)


