import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 200)

for r in range(1, 8):
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y)

plt.title("Expanding Circles")
plt.gca().set_aspect('equal')
plt.show()
