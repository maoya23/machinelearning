import pandas as pd

my_url=('https://raw.githubusercontent.com/taroyabuki''/fromzero/master/data/smoker.csv')
my_data=pd.read_csv(my_url)

print(my_data.head())

my_table=pd.crosstab(       #pd.crosstabでクロステーブル集計表を作成する。「はい」かつ「はい」が何人とかの表
my_data['alive'],
my_data['smoker']
)
print(my_table)

from scipy.stats import chi2_contingency
print('χ二乗検定のp値は{0}です。'.format(chi2_contingency(my_table,correction=False)[1]))
