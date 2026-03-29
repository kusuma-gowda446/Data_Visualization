

import matplotlib.pyplot as plt
import numpy as np

n = 5  # star points
theta = np.linspace(0, 2*np.pi, n*2+1)

r = np.array([1, 0.4] * n + [1])

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.title("Star Polygon")
plt.gca().set_aspect('equal')
plt.show()
