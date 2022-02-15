#正則化とは、回帰係数の大きさに応じたペナルティをかけて訓練することで過学習を避けることを目的とする。
#正則化するにあたって今回のデータなどでは温度の単位が摂氏であるが、これが絶対温度などに変更すると予測値が変わるために標準化しておく
import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
from sklearn.exceptions import ConvergenceWarning
from sklearn.linear_model import ElasticNet,enet_path
from sklearn.model_selection import GridSearchCV,LeaveOneOut
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from scipy.stats import zscore
warnings.simplefilter('ignore',ConvergenceWarning)#これ以降警告を表示しない

my_data=pd.read_csv('wine.csv')
X,y=my_data.drop(columns=['LPRICE2']),my_data['LPRICE2']

#一般にLAsso,Ridge,Elastic Netなどの手法が用いられる。Lassoは回帰係数の絶対値の和に比例するペナルティ、Ridgeは絶対値の和の二乗に比例するペナルティ、Elastic Netは両方を混合したもの。

A=2
B=0.1

my_pipeline=Pipeline([   #パイプラインで標準化とElastic Netを結合する
    ('sc',StandardScaler()),
    ('enet',ElasticNet(
        alpha=A,    #Aでペナルティの強さを調整
        l1_ratio=B))])  #Bでペナルティのバランスを調整
my_pipeline.fit(X,y)

my_enet=my_pipeline.named_steps.enet #pipelineでつないだ物のうちenetのものだけを取り出す
print(my_enet.intercept_)#my_enetの切片を示す。つまり全ての影響がない時のワインの価格をさす。

print(pd.Series(my_enet.coef_,index=X.columns))#indexをXのcolumnsにしてmy_enetの回帰係数をpandasで表示
#WRAINは使わないということがわかる。

my_test=pd.DataFrame([[500,17,120,2]])
print(my_pipeline.predict(my_test))


#これ以降ペナルティの強さと係数の関係の図示のためのコード。今はわからんでもいい。
As=np.e**np.arange(2,-5.5,-0.1)
B=0.1

_,my_path,_=enet_path(
    zscore(X),zscore(y),
    alphas=As,
    l1_ratio=B
)

pd.DataFrame(my_path.T,columns=X.columns,index=np.log(As)).plot(xlabel='log A (=log alpha)',ylabel='Coefficients')
plt.show()
plt.savefig('penalty')

#グラフ終わり

#パラメータの決定をパラメータチューニングで実行する

As=np.linspace(0,0.1,21)
Bs=np.linspace(0,0.1,6)

my_pipeline_=Pipeline([('sc',StandardScaler()),('enet',ElasticNet())])

my_search=GridSearchCV(estimator=my_pipeline_,param_grid={'enet__alpha':As,'enet__l1_ratio':Bs},cv=LeaveOneOut(),scoring='neg_mean_squared_error',n_jobs=-1).fit(X,y)
my_model=my_search.best_estimator_#最良モデル

print(my_search.best_params_)
