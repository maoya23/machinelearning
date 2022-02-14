#k分割交差検証はK分割して残りのk-1このデータを訓練データ、切った一個を検証データにするもの。
#この検証データはローテーションで全部のペアで使われるので結局k×k回検証と訓練を行う
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

my_data=sm.datasets.get_rdataset('cars','datasets').data
X,y=my_data[['speed']],my_data['dist']

my_model=LinearRegression()
my_model.fit(X,y)

my_scores=cross_val_score(my_model,X,y)#k分割交差検証を指定する
#デフォルトの設定では決定係数を5分割交差検証。これを明示するなら引数cv=5とscoring='r2'を与える
print(my_scores)#5つの決定係数を得る
print(my_scores.mean())#そもそも決定係数を平均するものなので平均をとる
#これが決定係数(検証)になる。検証と訓練を全部行って結果だけくれる。

#決定係数の代わりにRMSEを求めるときは
#my_scores=cross_val_score(my_model,X,y,scoring='neg_root_mean_aquared_error')




