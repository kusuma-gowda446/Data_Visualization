import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 20)

for t in theta:
    plt.plot([0, np.cos(t)], [0, np.sin(t)])

plt.title("Radial Pattern")
plt.gca().set_aspect('equal')
plt.show()
