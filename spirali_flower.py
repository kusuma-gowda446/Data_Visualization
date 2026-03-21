import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 8*np.pi, 1000)
r = theta * np.sin(5 * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.title("Spiral Flower")
plt.gca().set_aspect('equal')
plt.show()
