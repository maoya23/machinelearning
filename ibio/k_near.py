#pythonにおけるk近傍法はその数字を中心にKの個数を選ぶ
#近傍の値の出力変数を個数で平均したものが値になる
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt

my_data=sm.datasets.get_rdataset('cars','datasets').data
X,y=my_data[['speed']],my_data['dist']

my_model=KNeighborsRegressor()
my_model.fit(X,y)

tmp=pd.DataFrame({'speed':np.linspace(min(my_data.speed),max(my_data.speed),100)})
tmp['model']=my_model.predict(tmp)

pd.concat([my_data,tmp]).plot(x='speed',style=['o','-'])
plt.show()

y_=my_model.predict(X)

print(((y-y_)**2).mean()**0.5)
print(my_model.score(X,y))
print(np.corrcoef(y,y_)[0,1]**2)