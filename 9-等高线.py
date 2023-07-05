<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    #the function about height
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

#use plt.contourf to filling contours
#X,Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)#8代表等高线分成10部分

#use plt.contour to add contour lines
C = plt.contour(X, Y,f(X, Y),8,colors='black', linewidth=0.5)

#adding label
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
=======
import matplotlib.pyplot as plt
import numpy as np

def f(x, y):
    #the function about height
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3, 3, n)
y = np.linspace(-3, 3, n)
X, Y = np.meshgrid(x, y)

#use plt.contourf to filling contours
#X,Y and value for (X,Y) point
plt.contourf(X, Y, f(X, Y), 8, alpha=0.75, cmap=plt.cm.hot)#8代表等高线分成10部分

#use plt.contour to add contour lines
C = plt.contour(X, Y,f(X, Y),8,colors='black', linewidth=0.5)

#adding label
plt.clabel(C, inline=True, fontsize=10)

plt.xticks(())
plt.yticks(())
>>>>>>> 6642bd0 (2023年第一个版本)
plt.show()