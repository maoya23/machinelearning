import numpy as np
import pandas as pd
import warnings
import matplotlib.pyplot as plt
from sklearn.exceptions import ConvergenceWarning
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import cross_val_score,GridSearchCV,LeaveOneOut
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


my_data=pd.read_csv('wine.csv')
X,y=my_data.drop(columns=['LPRICE2']),my_data['LPRICE2']


#標準化を行った後にモデルの訓練

warnings.simplefilter("ignore",ConvergenceWarning)
my_pipeline=Pipeline([('sc',StandardScaler()),('mlp',MLPRegressor())])#MLPはニューラルネットワークのこと

my_pipeline.fit(X,y)

my_scores=cross_val_score(my_pipeline,X,y,cv=LeaveOneOut(),scoring='neg_mean_squared_error')
warnings.simplefilter("default",ConvergenceWarning)

print((-my_scores.mean())**0.5)#RMSE(LOOCV)

my_pipeline_=Pipeline([
    ('sc',StandardScaler()),
    ('mlp',MLPRegressor(tol=1e-5,   #改善したとみなす基準
    max_iter=5000))])   #改善するまでの反復数

my_layers=(1,3,5, #隠れ層が一層の時
(1,1),(3,1),(5,1),(1,2),(3,2),(5,2)#隠れ層が二層の時
)
my_params={'mlp__hidden_layer_sizes':my_layers}
my_search=GridSearchCV(estimator=my_pipeline,param_grid=my_params,cv=LeaveOneOut(),scoring='neg_mean_squared_error',n_jobs=-1).fit(X,y)

my_model=my_search.best_estimator_#最良モデル

print(my_search.best_params_) #最良のパラメータを表示
