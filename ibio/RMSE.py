#RMSEは残差の二乗平均の平方根のこと
#あくまで訓練データの当てはまりの良さしかわからん、精度は不明

import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
import numpy as np

my_data=sm.datasets.get_rdataset('cars','datasets').data
X,y=my_data[['speed']],my_data[['dist']]

my_model=LinearRegression()
my_model.fit(X,y)
y_=my_model.predict(X)
my_data['y_']=y_

pd.options.display.float_format=('{:.2f}'.format)#pandasのオプションで有効数字も表示できるようにしたもの
my_data['residual']=y-y_
print(my_data.head())

ax=my_data.plot(x='speed',y='dist',style='o',legend=False)#my_dataのプロットをどうするか
my_data.plot(x='speed',y='y_',style='-',legend=False,ax=ax)#my_modelのプロットをどうするか
ax.vlines(x=X,ymin=y,ymax=y_,linestyles='dotted')#残差のプロットをどう描くか　#ax.vlinesで垂直方向に線を引く
plt.show()

print("二乗平均平方根誤差は{0}です。".format(mean_squared_error(y,y_)**0.5))#二乗平均平方根誤差のライブラリ
#または(my_data['residual']**2).mean()**0.5

print("決定係数は{0}です".format(my_model.score(X,y)))
#my_model.score(X,y)は1-{SUM(観測値-予測値)^2/SUM(観測値-観測値平均)^2}

