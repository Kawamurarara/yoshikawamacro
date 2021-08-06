import numpy as np
import matplotlib.pyplot as plt
import japanize_matplotlib #日本語を有効化するモジュールをインポート
plt.rcParams['xtick.direction'] = 'in' #x軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['ytick.direction'] = 'in' #y軸の目盛線が内向き('in')か外向き('out')か双方向か('inout')
plt.rcParams['xtick.major.width'] = 1 #x軸主目盛り線の線幅
plt.rcParams['ytick.major.width'] = 1 #y軸主目盛り線の線幅
plt.rcParams['font.size'] = 10.5 #フォントの大きさ
plt.rcParams['axes.linewidth'] = 1 # 軸の線幅edge linewidth。囲みの太さ

fig = plt.figure(figsize=(8, 6))

#add_subplot()でグラフを描画する領域を追加する
ax1 = fig.add_subplot(3, 1, 1)
ax2 = fig.add_subplot(3, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)

#加速度原理による景気循環モデル
def business_cycle_model(t, c, v, A, Y, C, ΔY, I):
    #A⇨Y⇨C⇨ΔY⇨Iの順で計算するので、そのズレを反映
    def Y_model(A, Y, c, v):
        return (c+v)*Y[-1] - v*Y[-2] + A[-1]

    #本来はc*Y[-1]
    def C_model(c, Y):
        return c*Y[-2]

    def ΔY_model(Y):
        return Y[-1] - Y[-2]

    #本来はv*(Y[-1] - Y[-2])
    def I_model(v, Y):
        return v*(Y[-2] - Y[-3])

    #i = 0の時にAが100⇨200になるショックを与える
    for i in t:
        if i < 0:
            A.append(100)
            Y.append(500)
            C.append(400)
            ΔY.append(0)
            I.append(0)
        elif i == 0:
            A.append(200)
            Y.append(round(Y_model(A, Y, c, v)))
            C.append(round(C_model(c, Y)))
            ΔY.append(round(ΔY_model(Y)))
            I.append(round(I_model(v, Y)))
        else:
            A.append(100)
            Y.append(round(Y_model(A, Y, c, v)))
            C.append(round(C_model(c, Y)))
            ΔY.append(round(ΔY_model(Y)))
            I.append(round(I_model(v, Y)))

#定数
t = [i for i in range(-2,16)]
c = 0.8
v = 1.0
A = []
Y = []
C = []
ΔY = []
I = []

#モデルを実行
business_cycle_model(t, c, v, A, Y, C, ΔY, I)

#グラフの作成
line1_ax1 = ax1.plot(t, A, label="A")
line1_ax2 = ax2.plot(t, Y, label="Y")
line2_ax2 = ax2.plot(t, C, linestyle = "dashed", label="C")
line3_ax2 = ax2.plot(t, I, label="I")
line4_ax2 = ax2.plot(t, [0]*len(t), linestyle = "dashed")
ax1.set_ylim(0, 300)
ax1.set_xlim(-2, 15)
ax1.set_xticks(t)
ax2.set_ylim(-200, 800)
ax2.set_xlim(-2, 15)
ax2.set_xticks(t)
ax2.set_xlabel("加速度原理による景気循環")

#表の作成
row_labels=["A", "Y", "C", "ΔY", "I"]
column_labels=["%d" %i for i in t]
data=[A, Y, C ,ΔY, I]
ax3.table(cellText = data, rowLabels = row_labels, colLabels = column_labels, loc = "center")
ax3.axis('tight')
ax3.axis('off')

ax1.legend()
ax2.legend()
fig.tight_layout() 
plt.show()
