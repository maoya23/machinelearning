#パラメターチューニングの手法
#K近傍法を使うときに最良のKを決定する工程のこと

import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV,LeaveOneOut
from sklearn.neighbors import KNeighborsRegressor
import matplotlib.pyplot as plt


my_data=sm.datasets.get_rdataset('cars','datasets').data
X,y=my_data[['speed']],my_data['dist']

my_params={'n_neighbors':range(1,16)}#捜索範囲を1から15の範囲に指定する。

my_search=GridSearchCV(estimator=KNeighborsRegressor(),param_grid=my_params,cv=LeaveOneOut(),scoring='neg_mean_squared_error')
#GridSearchCVはscikit-learnのモジュールの種類で、estimatorはモデルを、param_gridは捜索対象のパラメータ一覧を、CVは交差検証の回数を指定する。

my_search.fit(X,y)#学習の実行(チューニング)

tmp=my_search.cv_results_ #チューニングの詳細
my_scores=(-tmp['mean_test_score'])**0.5 #RMSEの結果
my_results=pd.DataFrame(tmp['params']).assign(validation=my_scores)#データフレームの作成
print(my_results.head())#データフレームの表示

my_results.plot(x='n_neighbors',style='o-',ylabel='RMSE')#グラフとして可視化する手段
plt.savefig("tuning_result")
plt.show()

print(my_search.best_params_)#最良のパラメータを確認する。
print((-my_search.best_score_)**0.5)#最良のRMSEを計算する。

my_model=my_search.best_estimator#これで精度が最もよいモデルを取得する
y_=my_model.predict(X)
print(mean_squared_error(y_,y)**0.5)#学習済みモデルとのRMSEを計算する。