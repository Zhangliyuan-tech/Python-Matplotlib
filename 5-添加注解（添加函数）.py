import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)#生成从-1到1的50个点
y = 2*x+1

plt.figure(num=1, figsize=(8, 5))#在这里可以设置figure和设置在一个图中设置多个图像在一个figure中
plt.plot(x, y)

#gca = 'get current axis'边框的调整
ax = plt.gca()#这里设置的是显示图像的边框
ax.spines['right'].set_color('none')#right:右边框
ax.spines['top'].set_color('none')#top：上边框
ax.xaxis.set_ticks_position('bottom')#下边框
ax.yaxis.set_ticks_position('left')#左边框
ax.spines['bottom'].set_position(('data', 0))#这里是将x轴的位置确定在y轴的0这个值上
ax.spines['left'].set_position(('data', 0))#这里是将y轴的位置确定在x轴的0这个值上

x0 = 1
y0 = 2*x0 + 1
plt.scatter(x0, y0, s=250, color='b', )#散点图
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)#结果同matlab中绘制直线

#method 1
##########################
plt.annotate(r'$2x+1%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16, arrowprops=dict(arrowstyle='->', connectionstyle='arc3, rad=.2'))
#method 2
##########################
plt.text(-3.7, 3, r'$This\ is\ the\ some\ text.\ \mu\ \sigma_i\ \alpha_t$',
         fontdict={'size': 16, 'color': 'r'})

plt.show()