import matplotlib.pyplot as plt

plt.figure()
'''''
#将一个figure分成两行两列
plt.subplot(2, 2, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 3)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 2, 4)
plt.plot([0, 2], [0, 2])
'''''

#将一个figure分成两行,第一行是一列，第二行是三列
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 1])

plt.subplot(2, 3, 6)
plt.plot([0, 2], [0, 2])



plt.show()