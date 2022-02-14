import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score,LeaveOneOut
from sklearn.neighbors import KNeighborsRegressor

my_data=sm.datasets.get_rdataset('cars','datasets').data
X,y=my_data[['speed']],my_data['dist']

my_lm_scores=cross_val_score(LinearRegression(),X,y,cv=LeaveOneOut(),scoring='neg_mean_squared_error')
my_knn_scores=cross_val_score(KNeighborsRegressor(n_neighbors=5),X,y,cv=LeaveOneOut(),scoring='neg_mean_squared_error')

print((-my_lm_scores.mean())**0.5)
print((-my_knn_scores.mean())**0.5)


my_df=pd.DataFrame({
    'lm':-my_lm_scores,
    'knn':-my_knn_scores
})
print(my_df.head())

my_df.boxplot().set_ylabel("$r^2$")
plt.show()

from statsmodels.stats.weightstats import DescrStatsW
d=DescrStatsW(my_df.lm-my_df.knn)
print(d.ttest_mean(alternative='two-sided'))
print(d.tconfint_mean(alpha=0.05,alternative='two-sided'))

