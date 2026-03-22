import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 500)

for i in range(50):
    r = i * 0.1
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    plt.plot(x, y, color=plt.cm.plasma(i/50))

plt.title("Gradient Circle")
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
