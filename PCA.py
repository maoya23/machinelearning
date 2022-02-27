import numpy as np
import pandas as pd
from pca import pca
from scipy.stats import zscore
import matplotlib.pyplot as plt

my_data=pd.DataFrame(
    {'language':[0,20,20,25,22,17],
    'english':[0,20,40,20,24,18],
    'math':[100,20,5,30,17,25],
    'science':[0,20,5,25,16,23],
    'society':[0,20,30,0,21,17]},
    index=['A','B','c','d','e','f']
)

my_model=pca(n_components=5)
my_result=my_model.fit_transform(my_data)#主成分分析の実行

print(my_result['PC']) #主成分スコアの表示

my_model.biplot(legend=False)
plt.savefig("PCA.png")

