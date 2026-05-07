import matplotlib.pyplot as plt
import numpy as np

for i in range(50):
    x = np.random.rand(10)
    y = np.random.rand(10)
    plt.plot(x, y)

plt.show()
