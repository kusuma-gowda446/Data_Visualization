import matplotlib.pyplot as plt
import numpy as np

for angle in np.linspace(0, 2*np.pi, 12):
    x = [0, np.cos(angle)]
    y = [0, np.sin(angle)]
    plt.plot(x, y)

for r in np.linspace(0.2, 1, 6):
    circle = plt.Circle((0,0), r, fill=False)
    plt.gca().add_artist(circle)

plt.axis('equal')
plt.show()
