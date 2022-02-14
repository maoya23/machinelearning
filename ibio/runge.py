#ルンゲクッタ法で次の微分方程式を解け
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
    #x,yの初期値の設定
    x0=1.0
    y0=0.0
    #それぞれリストに追加
    x.append(x0)
    y.append(y0)
    #tを定義
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

    #x,yのリストより関数を図示
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x, y, color='r')
    plt.show()


#引数はx_i、y_i、dt、戻り値はx_i+1として、法によりdt後のxを計算する
def func_x(xi, yi, dt):
    #問題文よりdtの間のxの変化分は
    dx = yi
    #時間tにおけるxの数値計算量はルンゲクッタ
    xj = xi+dx*dt
    #x_i+1を返す
    return xj

#引数はx_i、y_i、dt、戻り値はy_i+1として、ルンゲクッタ法によりdt後のyを計算する
def func_y(xi, yi, dt):
    #k1の引数は、xi,yi,dtで関数func_fで計算
    k1 = func_f(xi, yi, dt)
    #k2の引数は、xi+dx/2,yi+k1/2,dtとして関数func_fで計算(dxはルンゲクッタの漸化式が一回進んだ時のxの変化量)
    k2 = func_f(func_x(xi, yi, dt/2), yi+k1/2, dt)
    #k3の引数は、xi+dx/2,yi+k2/2,dtとして関数func_fで計算(dxはルンゲクッタの漸化式が一回進んだ時のxの変化量)
    k3 = func_f(func_x(xi, yi, dt/2), yi+k2/2, dt)
    #k4の引数は、xi+dx,yi+k3,dtとして関数func_fで計算(dxはルンゲクッタの漸化式が一回進んだ時のxの変化量)
    k4 = func_f(func_x(xi, yi, dt), yi+k3, dt)
    #y_i+1の計算
    yj = yi + (k1+2*k2+2*k3+k4)/6
    #y_i+1を返す
    return yj

#ルンゲクッタ法においてk1,k2,k3,k4を計算するf(x,y,t)の関数を定義(dt時間当たりのyの変化量)
def func_f(x, y, dt):
    #問題文よりdtの間のyの変化分は
    dy =-x + y*(1-pow(x, 2))
    #時間dtにおけるyの変化量は
    k = dy*dt
    #y_i+1を返す
    return k

#初期値と刻み幅を入力してmain関数(数値計算を行う関数)に渡す
main(1.0, 0.0, 0.25)