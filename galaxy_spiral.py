import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 20*np.pi, 3000)
r = np.exp(0.05 * theta)

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.axis('equal')
plt.show()
