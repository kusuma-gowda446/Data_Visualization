import matplotlib.pyplot as plt
import numpy as np

for i in range(20):
    angle = i * np.pi / 10
    x = [0, np.cos(angle)]
    y = [0, np.sin(angle)]
    plt.plot(x, y)

plt.axis('equal')
plt.show()
