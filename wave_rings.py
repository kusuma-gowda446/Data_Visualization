import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 500)

for i in range(1, 15):
    r = i + 0.5*np.sin(6*theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y)

plt.title("Circular Wave Rings")
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
