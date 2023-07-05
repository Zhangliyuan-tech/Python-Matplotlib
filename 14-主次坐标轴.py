<<<<<<< HEAD
<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05*x**2
y2 = -1*y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()#在ax1中共享x坐标轴
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')


ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color='g')
ax2.set_ylabel('Y2', color='b')



=======
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05*x**2
y2 = -1*y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()#在ax1中共享x坐标轴
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')


ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color='g')
ax2.set_ylabel('Y2', color='b')



>>>>>>> 6642bd0 (2023年第一个版本)
=======
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y1 = 0.05*x**2
y2 = -1*y1

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()#在ax1中共享x坐标轴
ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b--')


ax1.set_xlabel('X data')
ax1.set_ylabel('Y1', color='g')
ax2.set_ylabel('Y2', color='b')



>>>>>>> 63023c4c8e7c4d8360bf409edb582225be0c1289
plt.show()