import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)#生成从-1到1的50个点
y1 = 2*x+1
y2 = x**2

plt.figure(num=1, figsize=(8, 5))#在这里可以设置figure和设置在一个图中设置多个图像在一个figure中
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.xlim((-1, 2))#设置x坐标轴的范围
plt.ylim((-2, 3))#设置y坐标轴的范围

plt.xlabel('I am x')#设置x轴的标签
plt.ylabel('I am y')


new_ticks = np.linspace(-1, 2, 5)#调整坐标轴的坐标间隔
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.8, -1, 1.22, 3],
            [r'$really\ good$', r'$bad$', r'$noraml$', r'$really\ good$'])#将y轴的值和字符串对应,绿字是latex语法

plt.show()