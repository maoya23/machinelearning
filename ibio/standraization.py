import pandas as pd
import matplotlib.pyplot as plt


#標準化する前のプロットを表示
my_data=pd.read_csv("wine.csv")
X=my_data.drop(columns=['LPRICE2'])
#X.boxplot(showmeans=True)
#plt.title('unstandarized')
#plt.savefig("boxplot")

from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

y=my_data['LPRICE2']

pd.DataFrame(StandardScaler().fit_transform(X),columns=X.columns).boxplot(showmeans=True)
plt.savefig("standarized boxplot")#標準化した後のグラフを表示する。

my_pipeline=Pipeline([('sc',StandardScaler()),('lr',LinearRegression())])#pipelineを使って標準化と線形モデルを組み合わせる。
my_pipeline.fit(X,y)#組み合わせたもので学習させる。

my_lr=my_pipeline.named_steps.lr #named_steps.(名前)でパイプラインでつないだもののうち、名前のものを取り出すという作業。
print(my_lr.intercept_)#回帰係数の表示

print(pd.Series(my_lr.coef_,index=X.columns))

my_test=[[500,17,120,2]]
print(my_pipeline.predict(my_test))


