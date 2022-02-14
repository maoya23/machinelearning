import matplotlib.pyplot as plt
import numpy as np

#plt.ごり押しcode
x=np.linspace(0,1,100)
y=x**2
plt.plot(x,y)
plt.show()

#オブジェクト指向インターフェース
x=np.linspace(0,1,100)
y=x**2
fig=plt.figure()         #figureオブジェクト生成#
ax=fig.add_subplot(111)  #axesオブジェクト生成、(数字は先頭から行、列、何番目か)#
ax.plot(x,y)
plt.show()

#  グラフサイズを指定してかつ複数表示する
x1=np.linspace(0,1,100)
y1=x1
x2=np.linspace(0,1,100)
y2=x2**2
x3=np.linspace(0,1,100)
y3=x3**3
x4=np.linspace(0,1,100)
y4=x4**4
fig,axes=plt.subplots(2,2,figsize=(10,6))
axes[0][0].plot(x1,y1)
axes[0][1].plot(x2,y2)
axes[1][0].plot(x3,y3)
axes[1][1].plot(x4,y4)

plt.show()


#axesを一次元に下げてfor文で回せるようにする
fig,axes=plt.subplots(2,2,figsize=(10,6))
one_dimension_axes=axes.ravel()#ravelで一次元配列に変更
x=np.linspace(0,1,100)
for i,ax in enumerate(one_dimension_axes):
    ax.plot(x,x**(i+1))
plt.show()

#二つのグラフを同じウィンドウに表示する
fig=plt.figure()
ax=fig.add_subplot(111)
x1=np.linspace(0,1,100)
y1=x1
x2=np.linspace(0,1,100)
y2=x2**2
ax.plot(x1,y1,label='y=x')
ax.plot(x2,y2,label='$y=x^2$')
ax.set_xlabel('x value')
ax.set_ylabel('y value')
plt.legend(loc='best')
plt.show()