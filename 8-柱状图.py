<<<<<<< HEAD
<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

#条形图显示y轴数据
for x,y in zip(X, Y1):
    #ha:horizontal alignment
    plt.text(x + 0.04, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x,y in zip(X, Y2):
    #ha:horizontal alignment
    plt.text(x + 0.04, -y - 0.05, '-%.2f' % -y, ha='center', va='top')

plt.xlim(-5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

=======
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

#条形图显示y轴数据
for x,y in zip(X, Y1):
    #ha:horizontal alignment
    plt.text(x + 0.04, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x,y in zip(X, Y2):
    #ha:horizontal alignment
    plt.text(x + 0.04, -y - 0.05, '-%.2f' % -y, ha='center', va='top')

plt.xlim(-5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

>>>>>>> 6642bd0 (2023年第一个版本)
=======
import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X/float(n))*np.random.uniform(0.5, 1.0, n)

plt.bar(X, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X, -Y2, facecolor='#ff9999', edgecolor='white')

#条形图显示y轴数据
for x,y in zip(X, Y1):
    #ha:horizontal alignment
    plt.text(x + 0.04, y + 0.05, '%.2f' % y, ha='center', va='bottom')
for x,y in zip(X, Y2):
    #ha:horizontal alignment
    plt.text(x + 0.04, -y - 0.05, '-%.2f' % -y, ha='center', va='top')

plt.xlim(-5, n)
plt.xticks(())
plt.ylim(-1.25, 1.25)
plt.yticks(())

>>>>>>> 63023c4c8e7c4d8360bf409edb582225be0c1289
plt.show()