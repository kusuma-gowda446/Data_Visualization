import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 50)

for t in theta:
    plt.plot([0, 10*np.cos(t)], [0, 10*np.sin(t)])

plt.title("Sunburst Pattern")
plt.gca().set_aspect('equal')
plt.axis('off')
plt.show()
