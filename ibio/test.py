#当たる確率が4/10のものを15回引いたらあたりが2回出た時の有意水準5%でp値を出す。
from statsmodels.stats.proportion import binom_test,proportion_confint

test=binom_test(
count=2,                    #当たった回数
nobs=15,                    #くじを引いた回数
prop=4/10,                  #当たる確率(仮説)、10回に4回当たるとする
alternative='two-sided')    #両側検定がデフォ、左側検定なら'smaller'右側検定なら'larger'

print(test)#帰無仮説棄却(4/10とは言えない)

#仮説検定の手順は
#1.有意水準を決める(ここでは5%)
#2.帰無仮説をθ=4/10、対立仮設をθ!=4/10とする
#3.帰無仮説のもとでp値を求める
#4.p値が有意水準より小さかったら帰無仮説棄却


#p値を理解するためにグラフを描画する
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats 

t=4/10  #当たる確率
n=15    #くじを引いた確率
x=np.array(range(0,n+1))    #当たった確率
my_pr=stats.binom.pmf(x,n,t)    #x回当たる確率
my_pr2=stats.binom.pmf(2,n,t)   #2回当たる確率

my_data=pd.DataFrame({'x':x,'y1':my_pr,'y2':my_pr})
my_data.loc[my_pr>my_pr2,'y1']=np.nan   #当たる確率が2回当たる確率を越えるもの
my_data.loc[my_pr<=my_pr,'y2']=np.nan   #当たる確率が2回当たる確率以下
ax=my_data.plot(x='x',style='o',ylabel='probability',figsize=(6,4),legend=False)
ax.hlines(y=my_pr2,xmin=0,xmax=15)
ax.vlines(x=x,  ymin=0,ymax=my_pr)
plt.show()

#グラフにおいて実現値以上に珍しいところを青でグラフにプロットした。これの和がp値になる


#15回引いたら2回当たるものの、有意水準5%での信頼区間(当たる確率としてあり得るもの)を求める
a=0.05
print(proportion_confint(
count=2,    #当たった回数
nobs=15,    #くじを引いた回数
alpha=a,    #有意水準
method='binom_test'
))

