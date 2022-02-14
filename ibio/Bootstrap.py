#15回引いて2回当たったくじを例としてブートストラップ法を考える。
import numpy as np
import matplotlib.pyplot as plt

X=[0]*13+[1]*2  #1: あたりを１、はずれを0とする

tmp=np.random.choice(X,15,replace=True) #2: Xから15回を復元抽出する。復元抽出は同じものを複数回並べるもの

sum(tmp)    #3: 当たった回数を求める

n=10**5
result=[sum(np.random.choice(X,len(X),replace=True))for _ in range(n)]  #4: 1から3を繰り返す。今回は10万回。_は変数名を使っていないという公示

plt.hist(result,bins=range(0,16))#ヒストグラムを描く
plt.show()

print(np.quantile(result,[0.025,0.975]))#結果の値の2.5%の値から97.5%の値のところを、信頼係数95%の信頼区間とみなす
#np.quantileは全体の分布を0.005と0.975に分割する点のこと

#当たる回数の信頼区間は[0,5]確率の信頼区間は[0,5/15]