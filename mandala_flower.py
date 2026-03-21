import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 500)

for i in range(1, 10):
    r = i * np.sin(5 * theta)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y)

plt.title("Mandala Pattern")
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
