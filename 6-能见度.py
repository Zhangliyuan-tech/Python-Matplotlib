import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)#生成从-1到1的50个点
y = 0.1*x

plt.figure()#在这里可以设置figure和设置在一个图中设置多个图像在一个figure中
plt.plot(x, y, linewidth=10, zorder=1)
plt.ylim(-2, 2)
#gca = 'get current axis'边框的调整
ax = plt.gca()#这里设置的是显示图像的边框
ax.spines['right'].set_color('none')#right:右边框
ax.spines['top'].set_color('none')#top：上边框
ax.xaxis.set_ticks_position('bottom')#下边框
ax.yaxis.set_ticks_position('left')#左边框
ax.spines['bottom'].set_position(('data', 0))#这里是将x轴的位置确定在y轴的0这个值上
ax.spines['left'].set_position(('data', 0))#这里是将y轴的位置确定在x轴的0这个值上

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_fontsize(12)
    label.set_bbox(dict(facecolor='white', edgecolor='None', alpha=0.7))

plt.show()