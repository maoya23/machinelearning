#重回帰分析は一つの出力値に対して複数の入力値があり、その結果訓練データに最もよく合うパラメータを見つける手法 今回はワインの価格を予測したい。
#重回帰分析の実態は行列計算である。
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score,LeaveOneOut

my_data=pd.read_csv("wine.csv")#csvファイルの読み込み

X,y=my_data.drop(columns=['LPRICE2']),my_data['LPRICE2']#XはLPRICE2を抜いたもの。yはLPRICEそのもの

my_model=LinearRegression().fit(X,y)

print(my_model.intercept_)#使ったモデルの切片を表示する。
print(pd.Series(my_model.coef_,index=X.columns))#coefは回帰変数のこと　indexのcolumnsをXのそれに指定してmy_modelのcoefを表示しろってこと

my_test=[[500,17,120,2]]#予測したい値を入れる
print(my_model.predict(my_test))

#以降当てはまりの良さ

y_=my_model.predict(X)

print(mean_squared_error(y_,y)**0.5)
