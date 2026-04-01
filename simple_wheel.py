import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 500)

for i in range(1, 20):
    r = i * 0.3
    x = r * np.cos(theta + i)
    y = r * np.sin(theta + i)
    plt.plot(x, y)

plt.title("Spinning Wheel Pattern")
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
