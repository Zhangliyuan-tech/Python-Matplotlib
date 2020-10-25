import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 50)#生成从-1到1的50个点
#y = 2*x+1
y = x**2
plt.plot(x, y)
plt.show()