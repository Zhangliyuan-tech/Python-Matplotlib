<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)#生成从-1到1的50个点
y1 = 2*x+1
y2 = x**2

plt.figure()#此处时figure的开头，以下输入的所有内容均和此figure有关
plt.plot(x, y1)

plt.figure(num=3, figsize=(8, 5))#在这里可以设置figure和设置在一个图中设置多个图像在一个figure中
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

=======
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)#生成从-1到1的50个点
y1 = 2*x+1
y2 = x**2

plt.figure()#此处时figure的开头，以下输入的所有内容均和此figure有关
plt.plot(x, y1)

plt.figure(num=3, figsize=(8, 5))#在这里可以设置figure和设置在一个图中设置多个图像在一个figure中
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

>>>>>>> 6642bd0 (2023年第一个版本)
plt.show()