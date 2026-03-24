import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 12*np.pi, 2000)

x = np.sin(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)
y = np.cos(t)*(np.exp(np.cos(t)) - 2*np.cos(4*t) - np.sin(t/12)**5)

plt.plot(x, y)
plt.title("Butterfly Curve")
plt.axis('off')
plt.gca().set_aspect('equal')
plt.show()
