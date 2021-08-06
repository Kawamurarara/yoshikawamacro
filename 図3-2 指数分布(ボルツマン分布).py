#https://qiita.com/skotaro/items/08dc0b8c5704c94eafb9を主に参考にした
import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語を有効化するモジュールをインポート
from matplotlib.ticker import ScalarFormatter #y軸の目盛りを10のべき乗表記にするモジュールをインポート
plt.rcParams['xtick.direction'] = 'in' #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in' #y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1 #x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1 #y軸主目盛り線の線幅
plt.rcParams['font.size'] = 10.5 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1 # 軸の線幅edge linewidth。囲みの太さ

#指数関数に従う、確率密度関数
def exp_dist(lambda_, x):
    return lambda_ * np.exp(-lambda_*x)

x = np.arange(0, 10000, 1)
s1, s2 = 0, 0
s = 0
for i in x:
    s1 += exp_dist(1.1*10**(-4),i)
    s2 += exp_dist(1.65*10**(-4),i)

y1= [exp_dist(1.1*10**(-4),i)/s1 for i in x]
y2= [exp_dist(1.65*10**(-4),i)/s2 for i in x]

#pyplotインターフェースからオブジェクト指向インターフェースに切り替え
fig = plt.figure() # Figureを作成
ax = fig.add_subplot(1,1,1) # Axesを作成

line1 = ax.plot(x, y1, label = "高い有効需要")
line2 = ax.plot(x, y2, linestyle = "dashed" ,label = "低い有効需要")

#y軸のメモリを10のべき乗表記にする
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style="sci",  axis="y",scilimits=(0,0))

ax.set_title("指数分布(ボルツマン分布)")
ax.set_xlabel("労働生産性")
ax.set_ylabel("各\n生\n産\n性\nを\n持\nつ\n企\n業\nで\n働\nく\n労\n働\n者\nの\nシ\nェ\nア", rotation=0, va='center')
ax.set_xlim(0,10000)
ax.legend()
plt.show()
