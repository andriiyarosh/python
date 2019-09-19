import numpy as np
import matplotlib.pyplot as plt

class1 = np.array([[0.05, 0.91],
                   [0.14, 0.96],
                   [0.16, 0.9],
                   [0.07, 0.7],
                   [0.2, 0.63]])

class2 = np.array([[0.49, 0.89],
                   [0.34, 0.81],
                   [0.36, 0.67],
                   [0.47, 0.49],
                   [0.52, 0.53]])

for i in enumerate(class1):
    p1, = plt.plot(class1[:, 0], class1[:, 1], '*r')

for i in enumerate(class2):
    p2, = plt.plot(class2[:, 0], class2[:, 1], '+b')

plt.legend([p1, p2], ["class1", "class2"])
plt.grid(True)
plt.show()
