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

#生産性の二乗のべき分布に従う職の数を表す関数
def f_jobs(x):
    if x < 50 :
        return 10
    if x >= 50:
        return 10*(50/x)*(50/x)

#β = -∞ の時の労働者を求める関数
#β = -∞ の時は、生産性がμより大きい時、職の数と労働者の数が一致する
def workers_1(x, μ):
    if x < μ:
        return 0
    else:
        return f_jobs(x)

#β = 0　の時の労働者数を求める関数
#β = 0　の時は労働者数は職の数の半分となる
def workers_2(x):
    
    return f_jobs(x)/2

x = np.arange(1, 201, 1)
μ = 25 #留保賃金μは25とする

y1 = [f_jobs(i) for i in x]
y2 = [workers_1(i, μ) for i in x]
y3 = [workers_2(i) for i in x]

#pyplotインターフェースからオブジェクト指向インターフェースに切り替え
fig = plt.figure() # Figureを作成
ax = fig.add_subplot(1,1,1) # Axesを作成

line = ax.plot(x, y1, linestyle = "dashed", label = "職の数")
line1 = ax.plot(x, y2, label = "β ≃ -∞")
line2 = ax.plot(x, y3, label = "β ≃ 0")

ax.set_title("総需要の水準が極端に高い、あるいは低いときの生産性(職の質)の分布")
ax.set_xlabel("生産性の水準")
ax.set_ylabel("労\n働\n者\n数", rotation=0, va='center')
ax.set_xlim(0,200)
ax.legend()
plt.show()
