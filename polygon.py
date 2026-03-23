import matplotlib.pyplot as plt
import numpy as np

n = 6  # number of sides
theta = np.linspace(0, 2*np.pi, n+1)

for i in range(1, 10):
    x = i * np.cos(theta)
    y = i * np.sin(theta)
    plt.plot(x, y)

plt.title("Polygon Pattern")
plt.gca().set_aspect('equal')
plt.show()
