#LOOCVによるグラフの予測性能の評価
#一つのみを検証データとして取り出して、そのほかを訓練データとして用いる。
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error ,r2_score
from sklearn.model_selection import cross_val_score,LeaveOneOut

my_data=sm.datasets.get_rdataset('cars','datasets').data
X,y=my_data[['speed']],my_data['dist']
my_model=LinearRegression().fit(X,y)
y_=my_model.predict(X)

my_scores1=cross_val_score(my_model,X,y,cv=LeaveOneOut(),scoring='neg_mean_squared_error')
my_scores2=cross_val_score(my_model,X,y,cv=LeaveOneOut(),scoring='neg_root_mean_squared_error')
print('これのRMSE(検証)は{0}です。'.format(-my_scores2.mean))