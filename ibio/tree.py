import graphviz
import pandas as pd
import statsmodels.api as sm
from sklearn import tree
import matplotlib.pyplot as plt

my_data=sm.datasets.get_rdataset('iris','datasets').data
print(my_data.head())
X,y=my_data.iloc[:,0:4],my_data.Species #ilocは取り出す行と列を行番号と列番号で指定する　「:」 だけで全ての行を選択する。「0:4]で0列目から３列目までを取得する。

my_model=tree.DecisionTreeClassifier(max_depth=2,random_state=0)#良さが同じ分岐が複数ある場合はその一つがランダムに出されるが、今回はそのランダムさを取り出さない。
my_model.fit(X,y)

my_dot=tree.export_graphviz(
    decision_tree=my_model,
    out_file=None,
    feature_names=X.columns,
    class_names=my_model.classes_,
    filled=True
)

graphviz.Source(my_dot)
plt.savefig('tree.png')
