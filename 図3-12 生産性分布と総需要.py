import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語を有効化するモジュールをインポート
from scipy.interpolate import make_interp_spline
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

#β != -∞　の時の労働者数を求める関数
def workers(β, μ, x):

        def exp_dist(β, μ, x, l):
            return np.exp(-(f_jobs(x) - l) * β * (μ-x))
        m, c = 0, 0 #分母をm、分子をcと_する
        x1 = np.arange(0, round(f_jobs(x),3)+1, 1)
        x2 = np.arange(0, round(f_jobs(x),3), 1)
        for i in x1:
            m += exp_dist(β, μ, x, i)
        for i in x2:
            c += (f_jobs(x)-i) * exp_dist(β, μ, x,f_jobs(x) - i)
        return  c/m

#線形の関数を描出するときに書く関数
def model_(β, μ, x, X, Y):
    model=make_interp_spline(X,Y)
    if x <= 50:
        return workers(β, μ, x)
    else:
        return model(x)
    
β1 = -0.05
β2 = -0.02
μ = 25 #留保賃金μは25とする
x=np.linspace(1,201,500)
X = [i for i in range(1, 50)]
for i in range(1,11)[::-1]:
    X.append(np.sqrt(25000/i))

#pyplotインターフェースからオブジェクト指向インターフェースに切り替え
fig = plt.figure() # Figureを作成
ax = fig.add_subplot(1,1,1) # Axesを作成

y = [f_jobs(i) for i in x]
Y1 = [workers(β1, μ, i) for i in X]
Y2 = [workers(β2, μ, i) for i in X]
#y1 = [model_(β1, μ, i, X, Y1) for i in x]
#y2 = [model_(β2, μ, i, X, Y2) for i in x]

line = ax.plot(x, y, linestyle = "dashed", label = "職の数")
line1 = ax.scatter(X, Y1, marker='.', label = "β ≃ -0.05")
line2 = ax.scatter(X, Y2, marker='.', label = "β ≃ -0.02")

ax.set_title("生産性分布と総需要")
ax.set_xlabel("生産性の水準")
ax.set_ylabel("労\n働\n者\n数", rotation=0, va='center')
ax.set_xlim(0,200)
ax.legend()
plt.show()
