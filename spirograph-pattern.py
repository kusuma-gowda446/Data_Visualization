import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 20*np.pi, 1000)

R, r, d = 5, 3, 5

x = (R - r) * np.cos(t) + d * np.cos((R - r) * t / r)
y = (R - r) * np.sin(t) - d * np.sin((R - r) * t / r)

plt.plot(x, y)
plt.title("Spirograph Pattern")
plt.gca().set_aspect('equal')
plt.show()
