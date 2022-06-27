import pandas as pd
from statsmodels.stats.weightstats import DescrStatsW
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f

df=pd.read_csv('GSE205349_N047-S1_processed_data_tmm.csv')
df_1=df.drop(columns=['chr','biotype','WT.6dpf.4','pex5KO.6dpf.2','Ensembl_ID'])
#df_2=df_1.set_index(df_1.columns[0])

X=df_1['WT.6dpf.1']
Y=df_1['pex5KO.6dpf.1']
a=0.05 
alt='two-sided'

d=DescrStatsW(np.array(X)-np.array(Y))
print(d.ttest_mean(alternative=alt)[1])#t検定の実行。これはp値

points=[np.array(X),np.array(Y)]
fig,ax=plt.subplots()
bp=ax.boxplot(points)
ax.set_xticklabels(['WT.6dpf.1','pex5KO.6dpf.1'])
plt.title('Gene Expression')
plt.grid()
plt.savefig('t_test.png') #正規化が行われているかの確認


def ftest(a, b):
    #　統計量Fの計算
    v1 = np.var(a, ddof=1)
    v2 = np.var(b, ddof=1)
    n1 = len(a)
    n2 = len(b)
    f_value = v1/v2

    # 帰無仮説が正しい場合にFが従う確率分を生成
    f_frozen = f.freeze(dfn=n1-1, dfd=n2-1)

    # 右側
    p1 = f_frozen.sf(f_value)
    # 左側
    p2 = f_frozen.cdf(f_value)
    # 小さい方の2倍がp値
    p_value = min(p1, p2) * 2

    # 統計量Fとp値を返す
    return f_value, p_value

f_value,p_value=ftest(X,Y)
print(f"p値:{p_value:1.3f}")#等分散　等分散ではない帰無仮説の棄却

