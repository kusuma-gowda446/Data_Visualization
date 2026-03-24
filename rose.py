import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 1000)

k = 5  # petals
r = np.cos(k * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.title("Rose Curve")
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
