import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 10*np.pi, 500)
r = theta

x = r * np.cos(theta)
y = r * np.sin(theta)

plt.plot(x, y)
plt.title("Spiral Pattern")
plt.gca().set_aspect('equal')
plt.show()
