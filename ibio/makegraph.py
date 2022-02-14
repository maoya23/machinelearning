#参考にしたURL　https://note.nkmk.me/python-pandas-plot/
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('exam.csv',encoding='UTF8')
ax=data.plot(x='nanowave',y='absorbe',label='sample1')
#複数のプロットを重ねる場合は1つ目のplot()で取得できるAxesSubplotを2つ目以降のplot()の引数axに指定する。
data.plot(x='nanowave1',y='absorbe1',color='r',label='sample2',ax=ax)
#散布図の場合のcode ax=data.plot.scatter(x='nanowave',y='absorbe',alpha=0.5,label='sample1')
# #data.plot.scatter(x='nanowave1',y='absorbe1',color='r',label='sample2',alpha=0.5,ax=ax)
plt.legend()
plt.xlabel('nanowave')
plt.ylabel('absorbe')
plt.title('shape of curve')
plt.grid(True)
#plt.savefig('shape.of.curve.png')#先にplt.show()を持ってくると真っ白のグラフが保存されるのでsavefigしてからplt.show()
plt.show()