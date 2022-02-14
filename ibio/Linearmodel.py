#線形単回帰モデルによる予測
#データに最もあうモデルを求める過程を訓練という。訓練に使うデータを訓練データという。

import statsmodels.api as sm
my_data=sm.datasets.get_rdataset('cars','datasets').data
X,y=my_data[['speed']],my_data[['dist']]
#データをstatsmodelsから読み込む

from sklearn.linear_model import LinearRegression
my_model=LinearRegression()#モジュールの中で線形単回帰分析のものを選ぶ
my_model.fit(X,y)#モデルを学習させる

tmp=[[21.5]]
print(my_model.predict(tmp))#.predictが予想値になる

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

tmp=pd.DataFrame({'speed':np.linspace(min(my_data.speed),max(my_data.speed),100)})#minからmaxの間を100区間に分ける
tmp['move of model']=my_model.predict(tmp)#tmpの後の[]で表示する名前を変えられる。
pd.concat([my_data,tmp]).plot(x='speed',style=['o','-'])#pd.concatでデータフレームを縦に結合できる。詳しいことはその都度調べること。
plt.show()

