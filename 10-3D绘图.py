<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

#X,Y Value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)#将X,Y两个量转到一个面中
R = np.sqrt(X**2+Y**2)
#height value
Z = np.sin(R)

#注意绘制3D图语句的参数定义，stride代表跨度，rstride=1, cstride=1分别代表行跨和列跨
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
#3D图的投影，zdir可以设置向哪个方向投影
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)
=======
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig)

#X,Y Value
X = np.arange(-4, 4, 0.25)
Y = np.arange(-4, 4, 0.25)
X, Y = np.meshgrid(X, Y)#将X,Y两个量转到一个面中
R = np.sqrt(X**2+Y**2)
#height value
Z = np.sin(R)

#注意绘制3D图语句的参数定义，stride代表跨度，rstride=1, cstride=1分别代表行跨和列跨
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.get_cmap('rainbow'))
#3D图的投影，zdir可以设置向哪个方向投影
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
ax.set_zlim(-2, 2)
>>>>>>> 6642bd0 (2023年第一个版本)
plt.show()