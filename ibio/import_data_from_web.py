#参考にする文献　https://note.nkmk.me/python-pandas-read-csv-tsv/
import pandas as pd
my_url='http://www.liquidasset.com/winedata.html'#取得してくるURLを指定する
tmp=pd.read_table(my_url,skiprows=62,nrows=38,sep='\\s+',na_values='.')#skiprowsで読み飛ばす行を指定　nrwosは読み込む行数　na_valuesは欠損値として扱うものの種類の指定
#read_csvもread_tableも変わらんカンマ区切りはcsv、タブ区切りはtable
my_data=tmp.iloc[:,2:].dropna()#欠損値のある行を消去
my_data.head()
print(my_data.shape)
my_data.to_csv('wine.csv',index=False)