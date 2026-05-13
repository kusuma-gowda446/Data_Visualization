import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 500)

y1 = np.sin(x)
y2 = -np.sin(x)

plt.plot(x, y1)
plt.plot(x, y2)

for i in range(0, 500, 20):
    plt.plot([x[i], x[i]], [y1[i], y2[i]])

plt.show()
