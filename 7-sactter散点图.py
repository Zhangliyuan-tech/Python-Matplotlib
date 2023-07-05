<<<<<<< HEAD
<<<<<<< HEAD
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)# for color value

#plt.scatter(X, Y, s=75, c=T, alpha=0.5)
plt.scatter(np.arange(5), np.arange(5))

#plt.xlim((-1.5, 1.5))
#plt.ylim((-1.5, 1.5))
plt.xticks(())
plt.yticks(())




=======
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)# for color value

#plt.scatter(X, Y, s=75, c=T, alpha=0.5)
plt.scatter(np.arange(5), np.arange(5))

#plt.xlim((-1.5, 1.5))
#plt.ylim((-1.5, 1.5))
plt.xticks(())
plt.yticks(())




>>>>>>> 6642bd0 (2023年第一个版本)
=======
import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)# for color value

#plt.scatter(X, Y, s=75, c=T, alpha=0.5)
plt.scatter(np.arange(5), np.arange(5))

#plt.xlim((-1.5, 1.5))
#plt.ylim((-1.5, 1.5))
plt.xticks(())
plt.yticks(())




>>>>>>> 63023c4c8e7c4d8360bf409edb582225be0c1289
plt.show()