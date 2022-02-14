#t検定は二つの標本の平均に有意な差があるかどうかを検定する。
#データは東京の気温と大阪の気温
from statsmodels.stats.weightstats import CompareMeans,DescrStatsW
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

X=[32.1,26.2,27.5,31.8,32.1,31.2,30.1,32.4,32.3,29.9,29.6,26.6,31.2,30.9,29.3]
Y=[35.4,34.6,31.1,32.4,33.3,34.7,35.3,34.3,32.1,28.3,33.3,30.5,32.6,33.3,32.2]

my_data=pd.DataFrame({'x':X,'y':Y})
print(my_data.describe())   #describe()でmeanなどを表示

a=0.05  #有意水準 デフォでは0.05 基本-信頼係数
alt='two-sided' #差があると言いたいときは両側検定、Xの平均が小さいと言いたいのなら左側検定　Xの平均が大きいといいたいなら右側検定

d=DescrStatsW(np.array(X)-np.array(Y))  #薬を飲んだ場合の前後の変化のように対標本の場合

print(d.ttest_mean(alternative=alt)[1]) #p値

print(d.tconfint_mean(alpha=a,alternative=alt)) #信頼区間

c=CompareMeans(DescrStatsW(X),DescrStatsW(Y))   #対標本ではない場合
ve='pooled'#母分散が等しいと仮定する時、仮定しない場合はunequal
print(c.ttest_ind(alternative=alt,usevar=ve)[1])   #p値
#print(c,tconfint_diff(alpha=a,alternative=alt,usevar=ve))#信頼区間

#差がないという帰無仮説を棄却する。つまり有意な差がある
my_data.boxplot(figsize=(8,6))
plt.title('temperature between Tokyo and Osaka')
plt.xlabel('city name')
plt.ylabel('temperature')
plt.show()
