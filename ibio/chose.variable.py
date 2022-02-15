#入力変数のモデルの良さとして変数を多く入れればモデルが良くなる訳ではないことを確かめる。
#v1,v2として関係ない変数をモデルに入れて確かめる。
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score,LeaveOneOut

my_data=pd.read_csv("wine.csv")

n=len(my_data)
my_data2=my_data.assign(v1=[i%2 for i in range(n)],v2=[i%3 for i in range(n)]) #my_dataに010101010 と012012012の列を追加する。

print(my_data2.head())

X,y=my_data2.drop(columns=['LPRICE2']),my_data2['LPRICE2']
my_model2=LinearRegression().fit(X,y)

y_=my_model2.predict(X)#訓練データから予測したデータの残差の計算
print(mean_squared_error(y_,y)**0.5)

my_scores=cross_val_score(my_model2,X,y,cv=LeaveOneOut(),scoring='neg_mean_squared_error') #検証データから出した精度からの残差の計算
print((-my_scores.mean())**0.5)

#実行すると訓練の方では当てはまりは良くなったが検証データの方では精度が悪くなった。つまり、変数は追加しないほうがよかった。

#半端な変数を追加するとかえって結果が悪くなるので必要な変数だけを選び取る方法を考える。(変数選択)
#今回はステップワイズ法のうち変数増加法を用いる(入力変数0このモデルから始めて、予測に役立ちそうな変数をひとつずつ追加する)

from sklearn.feature_selection import SequentialFeatureSelector
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline

my_sfs=SequentialFeatureSelector(
    estimator=LinearRegression(),#使用する外部推定機　このモデルに基づいて特徴の重要度を判別する。
    direction='forward',#変数増加法の指定
    cv=LeaveOneOut(),
    scoring='neg_mean_squared_error')

my_pipeline=Pipeline([('sfs',my_sfs),('lr',LinearRegression())]) #変数選択の後で再訓練できるようにするために、変数選択と回帰分析をパイプラインでつなぐ。

my_params={'sfs__n_features_to_select':range(1,6)} #n_features_to_selectで選択する特徴量を指定する。紺顔は1から6まで

my_search=GridSearchCV(estimator=my_pipeline,param_grid=my_params,cv=LeaveOneOut(),scoring='neg_mean_squared_error',n_jobs=-1).fit(X,y)#tuning.py参照
my_model=my_search.best_estimator_

print(my_search.best_estimator_.named_steps.sfs.get_support())

